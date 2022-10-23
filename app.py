from flask import Flask, request, jsonify, send_from_directory
import random
import backend.backend as backend

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
    return send_from_directory('client/public', 'index.html')

@app.get("/data/<UUID>")
def getReceiptData(UUID):
    return backend.getReceiptData(UUID)

@app.post("/data/")
def createReceipt():
    print("\n", request.data, "\n")
    return f"You have created a new recipt!"

@app.route("/data/{UUID}", methods=["PATCH"])
def updateReceipt(UUID):
    return f"You have updated the {UUID} recipt."



if __name__ == "__main__":
    app.run(debug=True)
