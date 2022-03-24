import pyautogui
import msvcrt
import os

CWD = os.getcwd()
IMAGES_PATH = 'images'
IMAGE_COOKIE = os.path.join(CWD, IMAGES_PATH, 'Cookie.png')
print(IMAGE_COOKIE)

while True:
    isCookie = pyautogui.screenshot(IMAGE_COOKIE)

    print(isCookie)

    if msvcrt.kbhit():
        break