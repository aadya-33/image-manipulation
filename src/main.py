import numpy as np
import cv2 as cv
import os
import sys
from image import flip_horizontal, flip_vertical, rotate_90deg_cw, rotate_180deg_cw, rotate_270deg_cw, crop, resize, rescale

# defining functions that only take user inputs greater than 0
def safe_input_float(str):
    while(True):
        usr_input = float(input(str))
        if usr_input > 0:
            return usr_input
        else: 
            continue

# directory where outputs are stored
os.makedirs("outputs", exist_ok=True)  

# image reading
path = input("Enter the pathname of the image: ");
img = cv.imread(path);

#checking if image is read properly
if img is None:
    sys.exit("Error: Could not read the image. Check the file path and re run the code")

else:
    print("Image loaded successfully!")

#interactive menu
while(True):
    print("Enter a choice: ")
    print("Transformation Menu:")
    print("1. Flip image horizontally")
    print("2. Flip image vertically")
    print("3. Rotate image by 90 degrees clockwise")
    print("4. Rotate image by 180 degrees clockwise")
    print("5. Rotate image by 270 degrees clockwise")
    print(f"6. Crop the image (image resolution : {img.shape[1]}x{img.shape[0]})")
    print("7. Resize the image")
    print("8. Rescale the image")
    print("0. Exit")
    choice = input("Enter your choice: ")

    #match-case construct
    match choice:
        case "1":
            img_flip_hor = flip_horizontal(img)
            pathname = "outputs/img_flip_h.jpg"
            ok = cv.imwrite(pathname, img_flip_hor)
            print(f"Edited image save at {pathname}\n" if ok else "File not saved\n")
        case "2":
            img_flip_ver = flip_vertical(img)
            pathname = "outputs/img_flip_v.jpg"
            ok = cv.imwrite(pathname, img_flip_ver)
            print(f"Edited image save at {pathname}\n" if ok else "File not saved\n")
        case "3":
            img_rot_90 = rotate_90deg_cw(img)
            pathname = "outputs/img_rot_90.jpg"
            ok = cv.imwrite(pathname, img_rot_90)
            print(f"Edited image save at {pathname}\n" if ok else "File not saved\n")
        case "4":
            img_rot_180 = rotate_180deg_cw(img)
            pathname = "outputs/img_rot_180.jpg"
            ok = cv.imwrite(pathname, img_rot_180)
            print(f"Edited image save at {pathname}\n" if ok else "File not saved\n")
        case "5":
            img_rot_270 = rotate_270deg_cw(img)
            pathname = "outputs/img_rot_270.jpg"
            ok = cv.imwrite(pathname, img_rot_270)
            print(f"Edited image save at {pathname}\n" if ok else "File not saved\n")
        case "6":
            x1 = int(safe_input_float("Enter the row from where cropping starts: "))
            x2 = int(safe_input_float("Enter the row where cropping ends: "))
            y1 = int(safe_input_float("Enter the column from where cropping starts: "))
            y2 = int(safe_input_float("Enter the column where cropping ends: "))
            img_cropped = crop(img, x1, y1, x2, y2)
            pathname = "outputs/img_cropped.jpg"
            ok = cv.imwrite(pathname, img_cropped)
            print(f"Edited image save at {pathname}\n" if ok else "File not saved\n")
        case "7":
            new_h = int(safe_input_float("Enter the new height of image: "))
            new_w = int(safe_input_float("Enter the new width: "))
            img_resize = resize(img, new_w, new_h)
            pathname = "outputs/img_resize.jpg"
            ok = cv.imwrite(pathname, img_resize)
            print(f"Edited image save at {pathname}\n" if ok else "File not saved\n")
        case "8":
            f = safe_input_float("Enter the factor through which the image should be scaled: ")
            img_scaled = rescale(img, f)
            pathname = "outputs/img_scaled.jpg"
            ok = cv.imwrite(pathname, img_scaled)
            print(f"Edited image save at {pathname}\n" if ok else "File not saved\n")
        case "0":
            break
        case _:
            print("Please enter a valid input")