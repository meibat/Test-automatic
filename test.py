import pyautogui
from time import sleep

while True:
    x, y = pyautogui.position()
    print ("Posicao atual do mouse:")
    print ("x = "+str(x)+" y = "+str(y))
    sleep(3)