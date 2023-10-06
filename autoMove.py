import pyautogui, time, datetime
from os import system

system('cls')

def autoMove():
    time.sleep(2)
    sTime = datetime.datetime.now().strftime('%X')
    print(f"Start time: {sTime}\n")
    sTime = datetime.datetime.strptime(sTime, "%H:%M:%S")
    n = 1
    while True:
        try:
            # x = datetime.datetime.now().strftime('%X')
            pyautogui.moveTo(250, 6)
            print("Mouse Moved !!")
            time.sleep(5)
            # pyautogui.moveTo(533, 457)
            # time.sleep(10)
            x = datetime.datetime.now().strftime('%X')
            pyautogui.click(clicks=1)
            print(f"Total clicked: {n}\n{x}\n")
            time.sleep(120)
            n += 1
        except:
            eTime = datetime.datetime.now().strftime('%X')
            print(f"End time: {eTime}")
            eTime = datetime.datetime.strptime(eTime, "%H:%M:%S")
            timeInterval = eTime - sTime
            print(f"\nProgram stop!!\nTotal run time: {timeInterval}")
            break

autoMove()