import numpy as np
import cv2 as cv
import os
import sys
from image import flip_horizontal, flip_vertical, rotate_90deg_cw, rotate_180deg_cw, rotate_270deg_cw, crop, resize, rescale, grayscale, negetive, brightness, contrast, threshold, box_blur, gaussian_blur

# defining functions that only take user inputs greater than 0
def safe_input_float(str):
    while(True):
        usr_input = float(input(str))
        if usr_input > 0:
            return usr_input
        else: 
            continue

# defining function that saves a file in /outputs
def save(pathname, img):
    ok = cv.imwrite(pathname, img)
    print(f"Edited image save at {pathname}\n" if ok else "File not saved\n")

# directory where outputs are stored
os.makedirs("outputs", exist_ok=True)  

# image reading
path = input("Enter the pathname of the image: ");
img = cv.imread(path);

#checking if image is read properly
if img is None:
    sys.exit("Error: Could not read the image. Check the file path and re run the code")

else:
    print("Image loaded successfully!\n")

#interactive menu
while(True):
    print("Enter a choice: \n")
    print("Transformation Menu:")
    print("1. Flip image horizontally")
    print("2. Flip image vertically")
    print("3. Rotate image by 90 degrees clockwise")
    print("4. Rotate image by 180 degrees clockwise")
    print("5. Rotate image by 270 degrees clockwise")
    print(f"6. Crop the image (image resolution : {img.shape[1]}x{img.shape[0]})")
    print("7. Resize the image")
    print("8. Rescale the image\n")

    print("Colour and intensity:")
    print("9. Convert to grayscale")
    print("10. Negetive/invert image")
    print("11. Adjust brightness")
    print("12. Adjust contrast")
    print("13. Treshold\n")

    print("Filters")
    print("14. Box blur")
    print("15. Gaussian blur")
    print("\n0. Exit")
    choice = input("Enter your choice: ")

    #match-case construct
    match choice:
        case "1":
            img_flip_hor = flip_horizontal(img)
            save("outputs/img_flip_h.jpg", img_flip_hor)
        case "2":
            img_flip_ver = flip_vertical(img)
            save("outputs/img_flip_v.jpg", img_flip_ver)
        case "3":
            img_rot_90 = rotate_90deg_cw(img)
            save("outputs/img_rot_90.jpg", img_rot_90)
        case "4":
            img_rot_180 = rotate_180deg_cw(img)
            save("outputs/img_rot_180.jpg", img_rot_180)
        case "5":
            img_rot_270 = rotate_270deg_cw(img)
            save("outputs/img_rot_270.jpg", img_rot_270)
        case "6":
            x1 = int(safe_input_float("Enter the row from where cropping starts: "))
            x2 = int(safe_input_float("Enter the row where cropping ends: "))
            y1 = int(safe_input_float("Enter the column from where cropping starts: "))
            y2 = int(safe_input_float("Enter the column where cropping ends: "))
            img_cropped = crop(img, x1, y1, x2, y2)
            save("outputs/img_cropped.jpg", img_cropped)
        case "7":
            new_h = int(safe_input_float("Enter the new height of image: "))
            new_w = int(safe_input_float("Enter the new width: "))
            img_resize = resize(img, new_w, new_h)
            save("outputs/img_resize.jpg", img_resize)
        case "8":
            f = safe_input_float("Enter the factor through which the image should be scaled: ")
            img_scaled = rescale(img, f)
            save("outputs/img_scaled.jpg", img_scaled)
        case "9":
            img_greyscale = grayscale(img)
            save("outputs/img_greyscale.jpg", img_greyscale)
        case "10":
            img_invert = negetive(img)
            save("outputs/img_invert.jpg", img_invert)
        case "11":
            per = safe_input_float("Enter the percentage incrase in brightness: ")
            img_bright = brightness(img, per)
            save("outputs/img_bright.jpg", img_bright)  
        case "12":
            per = safe_input_float("Enter the percentage increase in contrast: ")     
            img_contrast = brightness(img, per)
            save("outputs/img_contrast.jpg", img_contrast) 
        case "13":
            tresh = safe_input_float("Enter the treshold value (0 to 225): ")
            img_tresh = threshold(img, tresh)
            save("outputs/img_tresh.jpg", img_tresh)
        case "14":
            size = int(safe_input_float("Enter the size of the box filter: "))
            img_box_blur = box_blur(img, size)
            save("outputs/img_box_blur.jpg", img_box_blur)
        case "15":
            size = int(safe_input_float("Enter the size of the gaussian filter: "))
            img_gaussian_blur = gaussian_blur(img, size)
            save("outputs/img_gaussian_blur.jpg", img_gaussian_blur)
        case "0":
            break
        case _:
            print("Please enter a valid input")