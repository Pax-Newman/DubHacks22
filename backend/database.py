from typing import Tuple
from pymongo import MongoClient
from dotenv import dotenv_values
import uuid, base64

class Database:
    def __init__(self):
        config = dotenv_values(".env")

        self.mongodb_client = MongoClient(config["ATLAS_URI"])
        self.database = self.mongodb_client[config["DB_NAME"]]

        print(self.mongodb_client.list_database_names())
        print("Connected to the MongoDB database!")
    
    def createReceipt(self, title:str, lines:Tuple[str, int], tax:int, image:str):
        UUID = self.generate_UUID()
        lines = [ {"lineID": i, "itemName" : name, "price" : price} for i, (name, price) in enumerate(lines) ]
        users = []

        document = {"title" : title, "UUID" : UUID, "lines" : lines, "tax" : tax, "users" : users, "image" : image}
        self.database["Receipts"].insert_one(document)

    def getReceipt(self, UUID:str):
        return self.database["Receipts"].find_one({"UUID" : UUID})

    def generate_UUID(self):
        while True:
            new_uuid:str = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode("ascii")
            new_uuid = new_uuid.removesuffix("==")

            result = self.database["Receipts"].find({"UUID" : {"$exists" : True, "$eq" : new_uuid }})
            
            if len(list(result)) == 0:
                break
        return new_uuid

    def editReceipt(self, UUID, changes):
        receipt = self.getReceipt(UUID)
        
        # remove old user in the list if in it
        for i, user in enumerate(receipt["users"]):
            if user["userName"] == changes["userName"]:
                del receipt["users"][i]
                break

        # add new player to the list
        receipt["users"].append({"userName" : changes["userName"],
                                   "claims" : changes["claims"]   })
   

        # Remove all removed lines from lines list
        new_lines = []
        for i, line in enumerate(receipt["lines"]):
            if line["lineID"] not in changes["removals"]:
                new_lines.append(line)
            

        # Remove all removed lines from every user's claimed list
        for removal in changes["removals"]:
        
            for user in receipt["users"]:
                if removal in user["claims"]:
                    user["claims"].remove(removal)

        # Add all of the new lines to the lines list

        nextLineId = max(receipt["lines"], key=lambda l: l["lineID"])["lineID"] + 1
        for addition in changes["additions"]:
            receipt["lines"].append({"lineID": nextLineId, "name": addition["name"], "price": addition["price"]})
            
            #Search for the target user and add the new ID to their claims
            target_user = addition["user"]
            for current_user in receipt["users"]:
                if target_user == current_user["userName"]:
                    current_user["claims"].append(nextLineId)
                    break
            
            nextLineId += 1



        # Replace every updated line with it's new values
        for update in changes["updates"]:
            for line in receipt["lines"]:
                if update["lineID"] == line["lineID"]:
                    line["itemName"] = update["newName"]
                    line["price"] = update["newPrice"]
                    break



        

        self.database["Receipts"].update_one({"UUID" : UUID}, )
        


if __name__ == "__main__":
    db:Database = Database()

    result = db.getReceipt("rAkQjfxpR3-98bAb7zlEqw")
    print(result)