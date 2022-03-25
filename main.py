from tkinter import image_names
from PIL import Image
import pyautogui
import json
import os

CWD = os.getcwd()
IMAGES_PATH = 'images'
STOREITEMS_PATH = 'StoreItems'
IMAGE_COOKIE = os.path.join(CWD, IMAGES_PATH, 'Cookie.png')

class StoreItem:
    
    def __init__(self, name, image_fname):

        self.name = name
        self.image_fname = image_fname

        self.__CalculateAveragePixelValue__()

    def __CalculateAveragePixelValue__(self):
        image_path = os.path.join(CWD, IMAGES_PATH, STOREITEMS_PATH, self.image_fname)
        im = Image.open(image_path)

        pixel_values = im.getpixel((32,32))
        print(pixel_values)

class Cookie:

    def __init__(self, img):

        while True:

            cookie_location = pyautogui.locateOnScreen(img, confidence=0.7)
            if cookie_location:
                print('SUCCESS -- cookie found!')

                self.cookie_location = cookie_location
                break

            print('FAILURE -- failed to find cookie. Please adjust Cookie Clicker Window to be on main monitor.')

    def Click(self):
        pyautogui.moveTo(self.cookie_location)
        pyautogui.click()


def Init():
    pyautogui.PAUSE = 0.1

    x = ParseJSON('StoreItems.json')

    keys = x.keys()
    keys = list(keys)
    newItem = StoreItem(x[keys[0]]["ItemName"], x[keys[0]]["FileName"])

def ParseJSON(fname):
    file = open(fname, 'r')
    file_contents = json.load(file)
    return file_contents

if __name__ == '__main__':
    Init()

    #cookie = Cookie(IMAGE_COOKIE)

    # while True:

    #     cursor_pos = pyautogui.position()

    #     print(f'brightness of cursor position: {pyautogui.pixel(cursor_pos.x, cursor_pos.y)}')

    #     # click_location = pyautogui.locateOnScreen(IMAGE_CURSOR, confidence = 0.99)
    #     # if click_location:
    #     #     print('found cursor')
    #     # else:
    #     #     print('failed to find cursor')

    # while True:
    #     click_location = pyautogui.locateOnScreen(IMAGE_CURSOR, confidence=0.8)
    #     pos = pyautogui.position()
    #     print(pyautogui.pixel(pos.x, pos.y))
    #     if click_location != None :
    #         if not pyautogui.pixelMatchesColor(int(pos.x), int(pos.y), GREYED_RGB, tolerance=0):
    #             # pyautogui.moveTo(click_location)
    #             # pyautogui.click()
    #             print('clickable - not greyed')
    #             continue

    #     click_location = pyautogui.locateOnScreen(IMAGE_COOKIE, confidence=0.7)
    #     print(click_location)

    #     # if click_location != None:
    #     #     # pyautogui.moveTo(click_location)
    #     #     # pyautogui.click()