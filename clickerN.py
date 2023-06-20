import pyautogui as screen
import random
import time
import numpy
import cv2
import mss
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\Tesseract-OCR\tesseract.exe'


timeForOpen = {'top':920, 'left':905, 'width':70, 'height':30}
coinCount = {'top':730, 'left':935, 'width':80, 'height':40}

def CheckTimeArea():
    im = numpy.asanyarray(sct.grab(timeForOpen))
    #im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #CheckTimeAreaSavePhoto()
    text:str = pytesseract.image_to_string(im)
    return text.strip()

def CheckCoinCount():
    im = numpy.asanyarray(sct.grab(coinCount))
    #im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #CheckCoinCountSavePhoto()
    count:str = pytesseract.image_to_string(im)
    return count.strip()

def CheckTimeAreaSavePhoto():
    monitor = timeForOpen
    #output = "TimeArea-{top}x{left}_{width}x{height}.png".format(**monitor)
    output = "TimeArea.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)

def CheckCoinCountSavePhoto():
    monitor = coinCount
    #output = "CoinArea-{top}x{left}_{width}x{height}.png".format(**monitor)
    output = "CoinArea.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)

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
    
def ClearTimeArea(text:str):
    print()
    
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
        print(total)
        return total
    return ts

def WhereAmI():
    imgLive = cv2.imread(r"images/live_open2.png")
    imgHome = cv2.imread(r"images/home_open2.png") 
    imgBox = cv2.imread(r"images/need_time2.png.png") 
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
        secrt = WhereAmI()
        print(secrt)
        live_open = screen.locateCenterOnScreen("images/live_open2.png", confidence=0.9)
        if(live_open==None):
            live_counter=live_counter+1
        else:
            live_counter=0
        
        if(live_counter==5):
            print("Live isnt open")
            home_open = screen.locateCenterOnScreen("images/home_open2.png", confidence=0.8)
            print(home_open)
            screen.moveTo(690,90,1) #Live Logo at Home
            screen.click()
            live_counter=0
            time.sleep(5)
        
        """SEARH BOX"""
        box_one = screen.locateCenterOnScreen("images/t_box2.png", confidence=0.9)
        box_multi = screen.locateCenterOnScreen("images/t_box_multi2.png", confidence=0.9)
        if(not(box_one==None and box_multi==None)):
            print("TAPDIM")
            screen.moveTo(690,140,1)
            screen.click()


            needTimeCount = 0
            while True:
                time.sleep(0.5)
                x=700
                y=910
                x1= x+ random.randint(0,480)
                y1= y+ random.randint(0,50)
                
                need_time = screen.locateCenterOnScreen("images/need_time2.png", confidence=0.9)
                if(need_time == None):
                    needTimeCount = needTimeCount+1
                    print(needTimeCount)
                else:
                    
                    text:str = CheckTimeArea()
                    countText:str = CheckCoinCount()
                    if(not countText==None or not countText==''):
                        count = int(countText)
                    if(count<50 and not count==None):
                        GoNextFromBox()
                        break
                    print(text)
                    print(count)
                    #if(int(text.count)>=7):
                    #print(text.count)
                    sec = CalculateSec(text)
                    screen.moveTo(x1,y1,0,2)
                    screen.click()
                
                if(needTimeCount==2):
                    screen.moveTo(x1,y1,0,2)
                    screen.click()
                if(needTimeCount==7):
                    needTimeCount=0
                    screen.moveTo(x1,y1,0,2)
                    screen.click()
                    opened_box_count=opened_box_count+1
                    print("Opened box count: ")
                    print(opened_box_count)
                    break

        else:
            GoNext()



    sleep(1)
