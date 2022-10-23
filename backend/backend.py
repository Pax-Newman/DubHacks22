import json
import database as DB
from ocr_image import OCR 
from parse_receipt_text import parse_text


db = DB.Database()

def getReceiptData(UUID: str):
    dict = db.getReceipt(UUID)
    del dict["_id"]
    return dict

def to_json(dic):
    json_object = json.dumps(dic, indent = 4) 
    return json_object


if __name__ == "__main__":
    print(to_json(getReceiptData("M-CQt9WyTH6bymPxmMn2ag")))