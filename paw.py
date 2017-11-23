import time
import random
import pyautogui

TUX_SNIP = 'tux_snip.png'
U, D, L, R, F, N = 'up', 'down', 'left', 'right', ' ', 'n'

def whereami():
    print('accessible positive window size is {}'.format(pyautogui.size()))
    pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = True
    time.sleep(1)
    curr = None
    while True:
        if curr != pyautogui.position():
            curr = pyautogui.position()
            print(curr)

def orient_game_window(src_img):
    coord = pyautogui.locateOnScreen(src_img)
    if not coord:
        raise ValueError('can\'t find tux bye.')
    if isinstance(coord, list):
        raise ValueError('we found tux {} times, bye.'.format(len(coord)))
    print('found tux snip at {}'.format(str(coord)))
    return coord

def nostrat():
    ctrls = [U, L, R]
    num_insts = 10000
    with open('ctrl.txt', 'w') as fhandle:
        insts = [random.choice(ctrls) for _ in range(num_insts)]
        fhandle.write('\n'.join(insts))

def brobot():
    insts = nostrat()
    sx, sy, _, _ = orient_game_window(TUX_SNIP)
    pyautogui.moveTo(sx, sy, duration=0.25)
    pyautogui.click(sx, sy)
    pyautogui.typewrite(insts)
    print('Done.')

def nostratdamus():
    pyautogui.keyDown(U)
    time.sleep(3)
    pyautogui.keyDown(L)
    time.sleep(1)
    pyautogui.keyUp(L)
    time.sleep(1)
    pyautogui.keyDown(R)
    time.sleep(3)
    pyautogui.keyUp(R)
    time.sleep(4)
    pyautogui.keyUp(U)
    # :(
    # ctrls = [U, L, R]
    # ud_ctrls = map(lambda x: pyautogui.keyDown(x), ctrls).extend(map(lambda x: pyautogui.keyUp(x), ctrls))
    # print(ud_ctrls)
    # num_insts = 100
    # with open('ctrl.txt', 'w') as fhandle:
    #     insts = [random.choice(ctrls) for _ in range(num_insts)]
    #     fhandle.write('\n'.join(insts))

def wannadl():
    sx, sy, _, _ = orient_game_window(TUX_SNIP)
    pyautogui.moveTo(sx, sy, duration=0.25)
    pyautogui.click(sx, sy)
    nostratdamus()
    # [inst for inst in insts]
    print('Done.')

if __name__ == '__main__':
    # whereami()
    # brobot()
    # wannadl()
    wannadl()

