from pyautogui import *
import pyautogui
import time
import keyboard
import random

while True:
    detect = pyautogui.locateOnScreen(
        '/mnt/Data/Müll/Code/Python/Project/ImageRecognition/till.png', confidence=0.80, grayscale=True, region=(2560, 240, 637, 647))
    if detect != None:
        x, y = pyautogui.center(detect)
        pyautogui.click(x, y)
    else:
        print("i can not see it")
