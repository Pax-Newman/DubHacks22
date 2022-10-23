from cv2 import threshold
import pytesseract, cv2
from PIL import Image
import numpy as np

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#thresholding
def thresholding(image):
    print()

    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#Contrast
def contrast(pixvals):
    return ((pixvals - pixvals.min()) / (pixvals.max()-pixvals.min())) * 255

#dilation
def dilate(image):
    kernel = np.ones((2,2),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)


#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((2,2),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)

def save_np(np_img, step):
    img: Image = Image.fromarray(np_img)
    img.save(f"{step}.jpg")

def OCR(img: Image) -> str:
    np_img = np.asarray(img)

    np_img = get_grayscale(np_img)
    # save_np(np_img, "gray")
    
    np_img = remove_noise(np_img)
    # save_np(np_img, "noise")

    np_img = contrast(np_img).astype(np.uint8)
    # save_np(np_img, "contrast")

    np_img = dilate(np_img)
    # save_np(np_img, "dialate")
    
    np_img = canny(np_img)
    # save_np(np_img, "canny")


    # np_img = thresholding(np_img)
    # save_np(np_img, "thresh")

    img: Image = Image.fromarray(np_img)
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=" ./@1234567890ABCDEFGHIJkLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"'
    
    string = pytesseract.image_to_string(img, config=custom_config)
    
    return string
# Testing
if __name__ == "__main__":
    text: str = OCR(Image.open("fred.jpg"))
    print(text)
