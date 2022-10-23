from ocr_image import OCR 
from parse_receipt_text import parse_text

from PIL import Image

if __name__ == "__main__":
    text: str = OCR(Image.open("winco.jpg"))
    print(text)

    tuples = parse_text(text)

    print(*tuples, sep="\n")

