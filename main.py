import pyautogui
import os

CWD = os.getcwd()
IMAGES_PATH = 'images'
IMAGE_COOKIE = os.path.join(CWD, IMAGES_PATH, 'Cookie.png')
print(IMAGE_COOKIE)

pyautogui.PAUSE = 0.01

while True:
    cookie_location = pyautogui.locateOnScreen(IMAGE_COOKIE, confidence=0.5)

    if cookie_location != None:
        pyautogui.moveTo(cookie_location)
        pyautogui.click()