import pytesseract
import time
import telepot
import telepot.exception
from telepot.loop import MessageLoop
from PIL import Image
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

img2 = cv2.imread("imgs/foto.jpeg")
img2 = cv2.resize(img2, None, fx=1, fy=1)
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
cv2.imshow("img", adaptive_threshold)

config = "--psm 4"

img = pytesseract.image_to_string(adaptive_threshold, lang="por", config=config)
print(img)

cv2.waitKey(0)