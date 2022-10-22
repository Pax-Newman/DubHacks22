from flask import Flask, send_from_directory
import random

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def getMainPage():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.get("/<UUID>")
def getEditPage(UUID):
    return f"This is the {UUID} page!"

@app.get("/data/<UUID>")
def getReceiptData(UUID):
    return f"This is the data for the {UUID} recipt!"

@app.post("/data/")
def createReceipt():
    return f"You have created a new recipt!"

@app.route("/data/{UUID}", methods=["PATCH"])
def updateReceipt(UUID):
    return f"You have updated the {UUID} recipt."



if __name__ == "__main__":
    app.run(debug=True)
