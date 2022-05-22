from pynput.keyboard import Controller
# pynput is the library that allows to control and monitor input devices
import time
keyboard = Controller()
# C capital in Controller
def sentence(message):
    time.sleep(5)
    keyboard.type(message)

sentence("My name is srijan lamichhane")
# it is too faster so everybody will know it is done by bot
# so we will move to our next module.