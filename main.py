import pyautogui
import os

CWD = os.getcwd()
IMAGES_PATH = 'images'
IMAGE_COOKIE = os.path.join(CWD, IMAGES_PATH, 'Cookie.png')
IMAGE_CURSOR = os.path.join(CWD, IMAGES_PATH, 'Cursor.png')
GREYED_RGB = tuple((117,128,127))


def init():
    pyautogui.PAUSE = 0.1   

if __name__ == '__main__':
    init()

    while True:
        click_location = pyautogui.locateOnScreen(IMAGE_CURSOR, confidence=0.8)
        pos = pyautogui.position()
        print(pyautogui.pixel(pos.x, pos.y))
        if click_location != None :
            if not pyautogui.pixelMatchesColor(int(pos.x), int(pos.y), GREYED_RGB, tolerance=0):
                # pyautogui.moveTo(click_location)
                # pyautogui.click()
                print('clickable - not greyed')
                continue

        click_location = pyautogui.locateOnScreen(IMAGE_COOKIE, confidence=0.7)
        print(click_location)

        # if click_location != None:
        #     # pyautogui.moveTo(click_location)
        #     # pyautogui.click()