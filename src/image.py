import numpy as np
import cv2 as cv

def flip_horizontal(img):
    return img[:, ::-1]

def flip_vertical(img):
    return img[::-1, :]

def rotate_90deg_cw(img):
    return cv.transpose(img[::-1, :])

def rotate_180deg_cw(img):
    return img[::-1, ::-1]

def rotate_270deg_cw(img):
    return rotate_90deg_cw(rotate_180deg_cw(img))