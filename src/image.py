import numpy as np
import cv2 as cv

def flip_horizontal(img):
    return img[:, ::-1]

def flip_vertical(img):
    return img[::-1, :]