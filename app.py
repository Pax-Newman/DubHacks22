from waitress import serve
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

@app.get("/data/<UUID>")
def getReceiptData(UUID):
    result = backend.getReceiptData(UUID)
    if result is None:
        return "Bad UUID", 400
    else:
        return result

@app.post("/data/")
def createReceipt():
    UUID = backend.createReceipt(request.get_json(force=True))
    return UUID

@app.route("/data/{UUID}", methods=["PATCH"])
def updateReceipt(UUID):
    backend.updateReceipt(request.get_json(force=True))
    return backend.getReceiptData(UUID)



if __name__ == "__main__":
    if len(sys.argv) > 0 and sys.argv[0] == "WSGI":
        serve(app, host="0.0.0.0", port=8080)
    else:
        app.run(debug=True)
