import webbrowser
import time
import pyautogui as pg
from datetime import datetime
import pyperclip

def Search(keyword,eng=False):
    # 1- open webbrowser
    url = 'https://www.google.com'
    webbrowser.open(url)
    time.sleep(2) #หยุด 2 วินาที

    # 2- type: thailand
    if eng == True:
        pg.write(keyword,interval=0.25)
    else:
        pyperclip.copy(keyword)
        time.sleep(1)
        pg.hotkey('ctrl','v')
        
    # 3- enter
    pg.press('enter')
    time.sleep(2)
    # 4- screenshot

    dt = datetime.now().strftime('%Y-%m-%d %H-%M-%S ') #strftime.org
    pg.screenshot(dt+keyword + '.jpg') #,region=(100,100,300,500)
    time.sleep(1)
    pg.hotkey('ctrl','w')

Search('usd to thb',eng=True)
Search('ราคาน้ำมัน')


