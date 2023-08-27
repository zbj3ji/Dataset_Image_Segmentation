"""
File: generate_ds_segmentation.py
Author: Jan Zbirovsky
GitHub: https://github.com/zbj3ji/Dataset_Image_Segmentation/upload/main
Date:   Date when the script was created or last modified
Description: 
        Simple code to generate a simple dateset for image segmentation tasks

If you use this code, please cite my name and GitHub
"""

import cv2
import numpy as np
import os
import random

# params which have to be set
NUM_IMAGES = 15
STORAGE_PATH = 'E:\\data_sets\\shapes\\'

# Create folders for shapes, images, and masks
shape_folders = ["triangle", "rectangle", "circle"]
for shape_folder in shape_folders:
    os.makedirs(os.path.join(STORAGE_PATH, f"images/{shape_folder}"), exist_ok=True)
    os.makedirs(os.path.join(STORAGE_PATH, f"masks/{shape_folder}"), exist_ok=True)

# Function to generate a random filled triangle
def generate_triangle(size):
    img = np.zeros((size, size), dtype=np.uint8)
    p1 = (random.randint(10, size - 10), random.randint(10, size - 10))
    p2 = (random.randint(10, size - 10), random.randint(10, size - 10))
    p3 = (random.randint(10, size - 10), random.randint(10, size - 10))
    triangle_cnt = np.array([p1, p2, p3])
    cv2.drawContours(img, [triangle_cnt], 0, (255), thickness=cv2.FILLED)
    return img

# Function to generate a random filled rectangle
def generate_rectangle(size):
    img = np.zeros((size, size), dtype=np.uint8)
    x1 = random.randint(10, size - 50)
    y1 = random.randint(10, size - 50)
    x2 = x1 + random.randint(20, 40)
    y2 = y1 + random.randint(20, 40)
    cv2.rectangle(img, (x1, y1), (x2, y2), (255), thickness=cv2.FILLED)
    return img

# Function to generate a random filled circle
def generate_circle(size):
    img = np.zeros((size, size), dtype=np.uint8)
    center = (random.randint(20, size - 20), random.randint(20, size - 20))
    radius = random.randint(10, 30)
    cv2.circle(img, center, radius, (255), thickness=cv2.FILLED)
    return img

# Loop to generate and save images and masks
for shape_folder in shape_folders:
    for i in range(NUM_IMAGES):
        canvas = np.zeros((128, 128), dtype=np.uint8)
        mask = np.zeros((128, 128), dtype=np.uint8)

        if shape_folder == "triangle":
            img = generate_triangle(128)
        elif shape_folder == "rectangle":
            img = generate_rectangle(128)
        elif shape_folder == "circle":
            img = generate_circle(128)
        # Add other shape generation logic here if needed

        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        canvas = cv2.cvtColor(canvas, cv2.COLOR_GRAY2BGR)
        canvas[np.where(img > 0)] = color

        mask[np.where(img > 0)] = 255

        image_filename = os.path.join(STORAGE_PATH, f"images/{shape_folder}/{shape_folder}_image_{i}.png")
        mask_filename = os.path.join(STORAGE_PATH, f"masks/{shape_folder}/{shape_folder}_mask_{i}.png")

        cv2.imwrite(image_filename, canvas)
        cv2.imwrite(mask_filename, mask)

print(f"Generated {NUM_IMAGES} images and masks for each shape.")
