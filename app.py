from flask import Flask, request, jsonify, send_from_directory
import backend.backend as backend
import sys

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def getMainPage():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.get("/edit/<UUID>")
def getEditPage(UUID):
    return send_from_directory('client/public', 'index.html')

@app.route("/data/<UUID>", methods=["GET", "PATCH"])
def getReceiptData(UUID):
    if request.method == 'GET':
        result = backend.getReceiptData(UUID)
        if result is None:
            return "Bad UUID", 400
        else:
            return result
    else:
        backend.updateReceipt(UUID, request.get_json(force=True))
        return "OKAY"

@app.post("/data/")
def createReceipt():
    json_data = request.get_json(force=True)
    print(type(json_data))
    UUID = backend.createReceipt(json_data)
    return UUID



if __name__ == "__main__":

    app.run(debug=True)
