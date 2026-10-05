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

def crop(img, x1, y1, x2, y2):
    return img[x1:x2, y1:y2]

def resize(img, new_w, new_h):
    h, w = img.shape[:2]
    rows = (np.arange(new_h) * h / new_h).astype(int)
    cols = (np.arange(new_w) * w / new_w).astype(int)
    return img[rows][:, cols]

def rescale(img, factor):
    h, w = img.shape[:2]
    return resize(img, max(1, int(w * factor)), max(1, int(h * factor)))