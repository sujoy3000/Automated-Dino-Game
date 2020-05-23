import pyautogui
from PIL import Image , ImageGrab
import time



def hit(key):

    pyautogui.keyDown(key)


def isCollide_Day(data):

    # For Cactus

    for i in range(560, 596):

        for j in range(230, 265):

            if data[i, j] < 100:

                hit("up")

                return

    return


def isCollide_Night(data):

    for i in range(560, 596):

        for j in range(230, 265):

            if data[i, j] > 100:

                hit("up")

                return

    return


if __name__=="__main__":

    while True:

        image = ImageGrab.grab().convert('L')

        data = image.load()

        if( data[1000 , 300] < 100 ):

            isCollide_Night(data)

        else: isCollide_Day(data)
