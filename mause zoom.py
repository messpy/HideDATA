from tracemalloc import start
import pyautogui
import datetime
import time
import schedule
import math
import webbrowser
import random
url = "https://lull-compass.com/mypage"

def job():
    pyautogui.FAILSAFE = False
    webbrowser.open(url)
    print("時刻になりました")
    pyautogui.click(1365, 767)
    time.sleep(5)
    pyautogui.hotkey('Winleft', 'up')
    time.sleep(3)
    pyautogui.click(93, 206)
    time.sleep(3)
    pyautogui.click(1005, 439)
    time.sleep(3)
    pyautogui.click(800, 500)
    #pyautogui.click(699, 544)




now = time.strftime("%H:%M")
h,m = now.split(":")
print(now)
h,m = int(h),int(m)
if h < 10:
    if m < 30:
        t = "10:28"
elif h < 14:
    t = "13:58"
elif h < 17:
    t = "16:59"

    
print(t,"desu")
#AM11:00のjob実行を登録
#schedule.every().days.at("7:00").do(task)

while True:
    #schedule.run_pending()
    now = time.strftime("%H:%M")
    time.sleep(5)
    print(now,t)
    x = random.uniform(1,1000)
    pyautogui.click(x,1)
    if str(now) == t:
        print("{0}→{1}".format(t,now))
        break

job()
