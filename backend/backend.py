import json
import backend.database as DB
from backend.ocr_image import OCR 
from backend.parse_receipt_text import parse_text


db = DB.Database()

def getReceiptData(UUID: str):
    dict = db.getReceipt(UUID)
    del dict["_id"]
    return to_json(dict)

def to_json(dic):
    return json.dumps(dic, indent = 4)  


def decode_b64_img():
    pass

if __name__ == "__main__":
    print(getReceiptData("M-CQt9WyTH6bymPxmMn2ag"))