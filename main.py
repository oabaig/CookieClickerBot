from PIL import Image
import pyautogui
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
        self.average_pixel_value = self.__CalculateAveragePixelValue__(image)
        self.image_coordinates = self.LocateImage()
        
        image.close()

    def __CalculateAveragePixelValue__(self, image):

        size = image.size()

        pixel_values = image.getpixel((size[0] / 2, size[1] / 2))
        return (pixel_values[0] + pixel_values[1] +pixel_values[2]) / 3

    def LocateImage(self):
        return pyautogui.locateOnScreen(self.image_path, confidence=0.9)

    def Click(self):

        if self.image_coordinates:
            pyautogui.moveTo(self.image_coordinates)
            pyautogui.click()
        else:
            self.image_coordinates = self.LocateImage()


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
    pyautogui.PAUSE = 0.1

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

if __name__ == '__main__':
    items = Init()

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