import datetime
import time

import numpy as np
import cv2

from PIL import ImageGrab

def process_image(image):
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    processed_image = cv2.GaussianBlur(processed_image, (5,5), 0)
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
        # cv2.imshow('window', cv2.cvtColor(new_screen, cv2.COLOR_BGR2GRAY))
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def process_image_training(image):
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return processed_image

def grab_training():
    last_time = time.time()
    x = 720
    y = 450
    dx, dy = 600, 600
    frame_no = 0
    now_str = datetime.datetime.now().strftime('%m%d_%H%M%S')
    while True:
        frame_no += 1
        screen = np.array(ImageGrab.grab(bbox=(x, y, x + dx, y + dy)))
        print('loop took {} sec on frame {}'.format(time.time()-last_time, frame_no))
        last_time = time.time()
        # cv2.imshow('window', cv2.cvtColor(new_screen, cv2.COLOR_BGR2GRAY))
        # cv2.imshow('window', process_image_training(screen))
        cv2.imshow('window', screen)
        cv2.imwrite('training/{}_{}.png'.format(now_str, frame_no), screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    grab_training()

