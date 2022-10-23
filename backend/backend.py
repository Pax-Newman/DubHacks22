import json, io, base64
from PIL import Image
import backend.database as DB
from backend.ocr_image import OCR 
from backend.parse_receipt_text import parse_receipt


db = DB.Database()


def getReceiptData(UUID: str):
    dict = db.getReceipt(UUID)
    if dict is None:
        return None

    del dict["_id"]
    return to_json(dict)

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
    img.save("out.jpg")
    return img

def updateReceipt(UUID, json_data):
    db.editReceipt(UUID, json_data)

if __name__ == "__main__":
    print(getReceiptData("M-CQt9WyTH6bymPxmMn2ag"))