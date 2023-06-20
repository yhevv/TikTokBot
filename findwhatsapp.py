import pyautogui as screen
import random
import time
import numpy
import cv2
import mss
import pytesseract
import pyperclip
import win32clipboard as clip
import win32con
from io import BytesIO
from PIL import ImageGrab
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\Tesseract-OCR\tesseract.exe'


def FindWhatsapp():
    whatsapp_xy = screen.locateCenterOnScreen("images/whatsapp_logo.png", confidence=0.8)
    if(whatsapp_xy == None):
        return print("Whatsp cant found")
    else:
        return print(whatsapp_xy)
    
def FindBlueStack():
    emu_xy = screen.locateCenterOnScreen("images/emu_logo.png", confidence=0.8)
    if(emu_xy == None):
        return print("BlueStack cant found")
    else:
        return print(emu_xy)
    
while(True):
    time.sleep(1)
    FindWhatsapp()
    FindBlueStack()