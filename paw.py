import time
import pyautogui

if __name__ == '__main__':
    print('accessible window size is {}'.format(pyautogui.size()))
    pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = True
    time.sleep(1)
    curr = None
    while True:
        if curr != pyautogui.position():
            curr = pyautogui.position()
            print(curr)

