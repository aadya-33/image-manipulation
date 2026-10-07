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

def box_blur(img, size=3):
    p = size // 2
    h, w = img.shape[:2]

    pad = ((p, p), (p, p)) if img.ndim == 2 else ((p, p), (p, p), (0, 0))
    padded = np.pad(img.astype(np.float32), pad, mode="edge")

    out = np.zeros(img.shape, dtype=np.float32)
    for i in range(size):
        for j in range(size):
            out += padded[i:i + h, j:j + w]  

    out /= size * size                     
    return np.clip(out, 0, 255).astype(np.uint8)

def gaussian_blur(img, size=5, sigma=1.0):
    p = size // 2
    h, w = img.shape[:2]
    ax = np.arange(size) - p
    k = np.exp(-(ax ** 2) / (2 * sigma ** 2))
    k /= k.sum()

    pad = ((p, p), (p, p)) if img.ndim == 2 else ((p, p), (p, p), (0, 0))
    padded = np.pad(img.astype(np.float32), pad, mode="edge")

    tmp = np.zeros((h + 2 * p, w) + img.shape[2:], dtype=np.float32)
    for j in range(size):
        tmp += k[j] * padded[:, j:j + w]

    out = np.zeros(img.shape, dtype=np.float32)
    for i in range(size):
        out += k[i] * tmp[i:i + h]

    return np.clip(out, 0, 255).astype(np.uint8)

def alpha_blend(source, target, alpha=0.5):
    # resize source to target's size using your resize function
    source = resize(source, target.shape[1], target.shape[0])

    out = alpha * source.astype(float) + (1 - alpha) * target.astype(float)
    return np.clip(out, 0, 255).astype(np.uint8)

def sharpen(img, amount=1.0):
    blurred = gaussian_blur(img, 5, 1.0).astype(np.float32)
    result = img.astype(np.float32) + amount * (img - blurred)
    return np.clip(result, 0, 255).astype(np.uint8)