#In this program we will make it to type each character

from pynput.keyboard import Controller
import time
keyboard = Controller()

time.sleep(5)

for char in "My name is srijan lamichhane.":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.05)

