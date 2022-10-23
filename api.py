from flask import Flask

app = Flask(__name__)

@app.get("/")
def getMainPage():
    return "Main Page"

@app.get("/<UUID>")
def getEditPage(UUID):
    return f"This is the {UUID} page!"

@app.get("/data/<UUID>")
def getReceiptData(UUID):
    return f"This is the data for the {UUID} recipt!"

@app.post("/data/")
def createReceipt():
    return f"You have created a new recipt!"

@app.route("/data/{UUID}", metods=["PATCH"])
def updateReceipt(UUID):
    return f"You have updated the {UUID} recipt."