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

def rescale(img, factor=1.5):
    h, w = img.shape[:2]
    return resize(img, max(1, int(w * factor)), max(1, int(h * factor)))

def grayscale(img):
    b = img[:, :, 0] # exctracting the blue channel
    g = img[:, :, 1] # extracting the green channel
    r = img[:, :, 2] # extracting the red channel
    g = 0.114 * b + 0.587 * g + 0.299 * r # multiplying by certain weights, we get greyscale image
    return g.astype(int)

def negetive(img):
    return 255 - img

def brightness(img, percent=50):
    res = img.astype(np.float32) * (1 + percent / 100)
    return np.clip(res, 0, 255).astype(np.uint)

def contrast(img, percent=50):
    res = img.astype(np.float32) * (percent/100)
    return np.clip(res, 0, 255).astype(np.uint8)

def threshold(img, t=127):
    gray = img if img.ndim == 2 else grayscale(img)
    return np.where(gray > t, 255, 0).astype(np.uint8)