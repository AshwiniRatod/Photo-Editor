import cv2
import numpy as np
def crop_image(img, x =50,y =50 ,w = 200,h = 200):
    return img[y:y+h,x:x+w]