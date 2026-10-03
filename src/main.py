import numpy as np
import cv2 as cv
import os
from image import flip_horizontal, flip_vertical

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
        case "0":
            break
        case _:
            print("Please enter a valid input")