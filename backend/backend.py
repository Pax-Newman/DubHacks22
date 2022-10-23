import json, io, base64
import re, math
from PIL import Image
import backend.database as DB
from backend.ocr_image import OCR 
from backend.parse_receipt_text import parse_receipt


db = DB.Database()


def getReceiptData(UUID: str):
    dic = db.getReceipt(UUID)
    if dic is None:
        return None

    del dic["_id"]

    for user in dic["users"]:
        sum = 0
        for claim in user["claims"]:
            sum += get_line(dic, claim)

        user["totalPrice"] = sum

    return to_json(dic)

def get_line(dict, i):
    for line in dict["lines"]:
        if line["lineID"] == i:
            return math.ceil(line["price"] / count_claimers(dict, i))

def count_claimers(dict, i):
    count = 0
    for user in dict["users"]:
        if i in user["claims"]:
            count +=1
    return count
        

def to_json(dic):
    return json.dumps(dic, indent = 4)  

def from_json(json_data):
    return json.load(json_data)


def createReceipt(json_data: str):
    print(type(json_data))
    #dic = from_json(json_data)
    
    title = json_data["title"]
    b64_img = json_data["image"]

    img = decode_b64_img(b64_img)

    text:str = OCR(img)
    lines, tax = parse_receipt(text)
    img: Image = decode_b64_img(b64_img)

    return db.createReceipt(title, lines, tax, json_data["image"])

def decode_b64_img(b64_img):
    img  = Image.open(io.BytesIO(base64.decodebytes(bytes(b64_img, "utf-8"))))
    img.save("out.png")
    return img

def updateReceipt(UUID, json_data):
    db.editReceipt(UUID, json_data)

if __name__ == "__main__":
    print(getReceiptData("V_zz-3VERkqpXWvCIFZlXw"))