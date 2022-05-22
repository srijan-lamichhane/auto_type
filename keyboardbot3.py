# In this program we will make the computer to get the text itself 
# without me having to manually type the text.
# Here we use tesseract and cv2 for text detection and extraction.

from pynput.keyboard import Controller
import pytesseract
import pyautogui
import cv2
#opencv and cv2 are not the package name. opencv-python is an open source computer vision and machine learning software library.
import time

time.sleep(1)
keyboard = Controller()

#include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd =  r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


pyautogui.screenshot('chill.jpg', region=(881,671,789,95))

#Read image from which text needs to be extracted.
image = cv2.imread('chill.jpg')


def get_text(default):
    pass


# Convert the image to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
 
# Specify structure shape and kernel size.
# Kernel size increases or decreases the area
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect
# each word instead of a sentence.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
 
# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
 
# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
                                                 
 
# Creating a copy of image
im2 = image.copy()
 
# A text file is created and flushed
file = open("recognized.txt", "w+")
file.write("")
file.close()
 
# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
     
    # # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
     
    # Cropping the text block for giving input to OCR
    cropped = im2[y:y + h, x:x + w]
     
    # # Open the file in append mode
    file = open("recognized.txt", "a")
     
    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)
     
    # Appending the text into file
    file.write(text)
    file.write("\n")
     
    # Close the file
    file.close

line = "|"

for char in get_text(cv2.imread('chill.jpg')):
    if char != line:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.05)
    elif char == line:
        keyboard.press("I")
        keyboard.release("I")

print(get_text(cv2.imread('chill.jpg')))
