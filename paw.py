import time
import pyautogui

def whereami():
    print('accessible window size is {}'.format(pyautogui.size()))
    pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = True
    time.sleep(1)
    curr = None
    while True:
        if curr != pyautogui.position():
            curr = pyautogui.position()
            print(curr)

def orient_game_window(src_img):
    test = pyautogui.locateOnScreen(src_img)
    print(test)

if __name__ == '__main__':
    # whereami()
    src_img = 'tux_snip.png'
    orient_game_window(src_img)
