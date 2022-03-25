from PIL import Image
import pyautogui
import asyncio
import json
import os

CWD = os.getcwd()
IMAGES_PATH = 'images'
STOREITEMS_PATH = 'StoreItems'

class StoreItem:
    
    def __init__(self, name, image_fname):

        self.name = name
        self.image_path = os.path.join(CWD, IMAGES_PATH, STOREITEMS_PATH, image_fname)
        image = Image.open(self.image_path)
        self.image_width, self.image_height = image.size
        pixels = image.getpixel((self.image_width / 2, self.image_height / 2))
        self.average_pixel_value = self.__CalculateAveragePixelValue__(pixels)
        self.image_coordinates = self.LocateImage()
        
        image.close()

    def __CalculateAveragePixelValue__(self, p):
        return (p[0] + p[1] + p[2]) / 3

    def LocateImage(self):
        return pyautogui.locateOnScreen(self.image_path, confidence=0.9)

    def Clickable(self):
        if self.image_coordinates:
            box = self.image_coordinates
            pixels = pyautogui.pixel(
                int(int(box.left) + int(box.width) / 2), 
                int(int(box.top) + int(box.height) / 2)
            )
            avg_pixels = self.__CalculateAveragePixelValue__(pixels)

            print(f'{self.average_pixel_value} {avg_pixels}')

            if not (avg_pixels < self.average_pixel_value):
                print(f'clicked {self.name} {self.average_pixel_value} {avg_pixels}')
                return True
            
            return False
        
        self.image_coordinates = self.LocateImage()
        print(f'try to find image {self.name} {self.image_coordinates}')
        return False

    def Click(self):
        pyautogui.moveTo(self.image_coordinates)
        pyautogui.click()

    def Print(self):
        print(f'name: {self.name} \t | \t average pixel value: {self.average_pixel_value}')

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
    pyautogui.PAUSE = 0.01

    items_json = ParseJSON('StoreItems.json')

    keys = items_json.keys()
    keys = list(keys)

    items = list()
    for key in keys:
        newItem = StoreItem(items_json[key]["ItemName"], items_json[key]["FileName"])
        items.append(newItem)

    return items

def ParseJSON(fname):
    file = open(fname, 'r')
    file_contents = json.load(file)
    return file_contents

async def CheckItemAvailable(items: list):
        
    for item in reversed(items):
        if item.Clickable():
            return item

    return None

if __name__ == '__main__':
    items = Init()

    cookie = Cookie(os.path.join(CWD, IMAGES_PATH, 'Cookie.png'))
    while True:
        item = asyncio.run(CheckItemAvailable(items))   
        if item:
            item.Click()
        else:
            cookie.Click()