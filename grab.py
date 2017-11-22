import numpy as np
from PIL import ImageGrab
import cv2
import time

def process_image(image):
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    processed_image = cv2.Canny(processed_image, threshold1=150, threshold2=150)
    return processed_image

def screen_record():
    last_time = time.time()
    x = 700
    y = 600
    dx, dy = 650, 500
    while True:
        screen = np.array(ImageGrab.grab(bbox=(x, y, x + dx, y + dy)))
        print('loop took {} sec'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_image(screen)
        #cv2.imshow('window', cv2.cvtColor(new_screen, cv2.COLOR_BGR2GRAY))
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()
