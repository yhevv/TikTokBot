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


timeForOpen = {'top':920, 'left':905, 'width':70, 'height':30}
coinCount = {'top':720, 'left':920, 'width':150, 'height':60}

def CheckTimeArea():
    im = numpy.asanyarray(sct.grab(timeForOpen))
    #im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #CheckTimeAreaSavePhoto()
    text:str = pytesseract.image_to_string(im)
    return text.strip()

def CheckTimeAreaSavePhoto():
    monitor = timeForOpen
    #output = "TimeArea-{top}x{left}_{width}x{height}.png".format(**monitor)
    output = "TimeArea.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)

def CheckCoinCount():
    im = numpy.asanyarray(sct.grab(coinCount))
    #im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    CheckCoinCountSavePhoto()
    count:str = pytesseract.image_to_string(im)
    print(count)
    count = count.strip()
    count = count.lstrip("©»>»()96OoD")
    count = count.strip()
    return count

def CheckCoinCountSavePhoto():
    monitor = coinCount
    #output = "CoinArea-{top}x{left}_{width}x{height}.png".format(**monitor)
    output = "CoinArea.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)
    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)

def GoNextWithCheck():
    screen.moveTo(690,140)
    screen.click()
    time.sleep(0.5)
    screen.moveTo(900,900)
    screen.mouseDown()
    screen.moveTo(900,90,1)
    screen.mouseUp()

def GoNext():
    screen.moveTo(900,900)
    screen.mouseDown()
    screen.moveTo(900,90,1)
    screen.mouseUp()

def GoNextFromBox():
    screen.moveTo(940,70)
    screen.click()
    GoNext()

def IsTimeFormat(text:str):
    if(text[0]=="0"):
        return True
    return False
    
def CalculateSec(ts:str):
    tdak=0
    tsan=0
    total=0
    if(not ts==None and not ts =='Open'):
        ts = ts.rstrip("\n")
        tsList = ts.split(":")
        
        tdak=int(tsList[0])
        tsan=int(tsList[1])
        total=tdak*60 + tsan
        #print(total)
        return total
    return -1

def AmIAtLive():
    live_open = screen.locateCenterOnScreen("images/live_open2.png", confidence=0.7)
    if(live_open == None):
        return False
    else:
        return True
    
def AmIAtHome():
    home_open = screen.locateCenterOnScreen("images/home_open2.png", confidence=0.8)
    if(home_open == None):
        return False
    else:
        return True

def AmIAtBox():
    box_time = screen.locateCenterOnScreen("images/need_time2.png", confidence=0.8)
    if(box_time == None):
        return False
    else:
        return True

def AmIAtSomeoneProfile():
    live_open = screen.locateCenterOnScreen("images/xxx.png", confidence=0.9)
    if(live_open == None):
        return False
    else:
        return True

def GoLiveFromHome():
    screen.moveTo(690,90,0,5) #Live Logo at Home
    screen.click()
    time.sleep(5)
        
def SpamBox():
    x1=940
    y1=935
    x=0
    while x<11:
        time.sleep(1)
        screen.moveTo(x1,y1,0,2)
        screen.click()
        print(x)
        x=x+1

def CheckBox():
    box_one = screen.locateCenterOnScreen("images/t_box2.png", confidence=0.9)
    if(box_one==None):
        return False
    else:
        return True

def CheckBoxMulti():
    box_multi = screen.locateCenterOnScreen("images/t_box_multi2.png", confidence=0.9)
    if(box_multi==None):
        return False
    else:
        return True

def FoundBox():
    print("TAPDIM")
    screen.moveTo(690,140,0.5)
    screen.click()

def BackLiveFromBox():
    screen.moveTo(940,180,0.5)
    screen.click()
    time.sleep(0.5)

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


def WhereAmI():
    imgLive = cv2.imread(r"images/live_open2.png")
    imgHome = cv2.imread(r"images/home_open2.png") 
    imgBox = cv2.imread(r"images/need_time2.png") 
    live_open = screen.locateCenterOnScreen(imgLive, confidence=0.9)
    home_open = screen.locateCenterOnScreen(imgHome, confidence=0.8)
    box_time = screen.locateCenterOnScreen(imgBox, confidence=0.9)

    if(live_open == None):
        if(home_open == None):
            if(box_time == None):
                return "IdontKnow"
            else:
                return "OnBox"
        else:
            return "OnHome"
    else:
        return "OnLive"
    
def ShareWithTikTok():
    screen.moveTo(1190,990,1)
    screen.click()

def CopyUsername():
    screen.moveTo(690,65,1)
    screen.click()
    screen.moveTo(710,770,1)
    screen.click()
    time.sleep(2)
    screen.moveTo(935,220,1)
    screen.click()
    username = pyperclip.paste()
    print(username)
    GoLiveFromProfile()
    return username

def GoBackTikTokApp():
    screen.moveTo(990,1060,1)
    screen.click()

def FindWhatsappProfile():
    screen.moveTo(170,150,0.5)
    screen.click()
    pyperclip.copy("TikTokLives")
    screen.hotkey('ctrl', 'v')
    screen.press('enter')
    screen.moveTo(120,235,0.5)
    screen.click()
    screen.moveTo(850,990,0.5)
    screen.click()
    
def ShareWithWhatsapp(message:str="error"):
    screen.moveTo(940,1050,0.5)
    screen.click()
    FindWhatsappProfile()
    #paste and enter
    
    pyperclip.copy(message)
    screen.hotkey('ctrl', 'v')
    screen.press('enter')

def MessageBuilder(username:str="Empty", sec:int=-1, coin:int=-1, link:str="error"):
    sec = sec-20 #time difference
    message:str = str("Username: "+ username + "\nTime(sec): " + str(sec) + "\nCoin Count: " + str(coin) + "\nLink: " + link)
    return message

def CopyLiveLink():
    screen.moveTo(1190,990,1)
    screen.click()
    screen.moveTo(710,850,1)
    screen.click()
    #screen.click()
    time.sleep(1)
    link = pyperclip.paste()
    return link

def GoLiveFromProfile():
    screen.moveTo(690,85,0.5)
    screen.click()

def SERVICE_ShareWithWhatsapp(sec:int, coin:int):
    pyperclip.copy("")
    BackLiveFromBox()
    #username = CopyUsername()
    link = CopyLiveLink()
    message = MessageBuilder(username="Empty",sec=sec,coin=coin, link=link)
    #FindWhatsapp()
    ShareWithWhatsapp(message=message)
    GoBackTikTokApp()
    GoNext()

    

##############################################3

name = screen.prompt(text="START ?",title="TikTokBot")+ "hey"


"""with mss.mss() as sct:
    while True:
        Im:str = WhereAmI()

        match Im:
            case "OnLive":
                print("Im OnLive")
            case "OnHome":
                print("Im OnHome")
            case "OnBox":
                print("Im OnBox")
            case _:
                print("WHO AM I")"""

opened_box_count=0
live_counter=0

with mss.mss() as sct:
    while True:
        time.sleep(5)
        AtLive:bool = AmIAtLive()
        AtHome:bool = AmIAtHome()
        AtBox:bool = AmIAtBox()

        #sect = WhereAmI()
        #print(sect)

        if(AtLive):
            print("I am at Live: ")
            print(AtLive)
            live_counter =0

            if(CheckBox() or CheckBoxMulti()):
                FoundBox()
                
            else:
                GoNextWithCheck()
            
        elif(AtHome):
            print("I am at Home: ")
            print(AtHome)
            live_counter=0
            GoLiveFromHome()

        elif(AtBox):
            time.sleep(1)
            live_counter =0
            print("I am at Box: ")
            print(AtBox)
            coinArea = CheckCoinCount()
            coinC = int(coinArea)
            timeArea = CheckTimeArea()
            timeSec = CalculateSec(timeArea)
            print("Coin Area: ")
            print(coinArea)
            print("Time Area: ")
            print(timeSec)
            if(coinC>99):
                SERVICE_ShareWithWhatsapp(timeSec,coinArea)
            else:
                BackLiveFromBox()
                GoNext()

            #SpamBox()

        else:
            live_counter=live_counter+1
            print("Where am I ?")
            BackLiveFromBox()
            if(live_counter==3):
                live_counter=0
                GoNextWithCheck()
            
