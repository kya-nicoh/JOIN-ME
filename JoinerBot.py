from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con

# X: 1424 Y:  831 RGB: ( 34,  43,  93)

int x = 0

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def joinMechanic():
    pic = pyautogui.screenshot()
    
    if pyautogui.locateOnScreen('join-button.png', grayscale=True, confidence=0.8) != None:
        for x in range(0, 1920, 5):
            for y in range(0, 1080, 5):

                r, g, b = pic.getpixel((x,y))
                
                if b == 93:
                    click(x, y)
                    print('DONEEE BITCHHH')
                    x = 1
                    time.sleep(0.05)
                    break
    else:
        print('====')
        time.sleep(0.05)

while keyboard.is_pressed('q') == False || x = 0:
    joinMechanic()
