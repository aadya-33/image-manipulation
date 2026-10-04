import numpy as np
import cv2 as cv
import os
from image import flip_horizontal, flip_vertical, rotate_90deg_cw, rotate_180deg_cw, rotate_270deg_cw

# directory where outputs are stored
os.makedirs("outputs", exist_ok=True)  

# image reading
path = input("Enter the pathname of the image: ");
img = cv.imread(path);

#checking if image is read properly
if img is None:
    print("Error: Could not read the image. Check the file path!")
else:
    print("Image loaded successfully!")

#interactive menu
while(True):
    print("Enter a choice: ")
    print("1. Flip image horizontally")
    print("2. Flip image vertically")
    print("3. Rotate image by 90 degrees clockwise")
    print("4. Rotate image by 180 degrees clockwise")
    print("5. Rotate image by 270 degrees clockwise")
    print("0. Exit")
    choice = input("Enter your choice: ")
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
        case "0":
            break
        case _:
            print("Please enter a valid input")