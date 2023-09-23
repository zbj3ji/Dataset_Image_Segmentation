"""
File: generate_ds_segmentation.py
Author: Jan Zbirovsky
GitHub: https://github.com/zbj3ji/Dataset_Image_Segmentation/upload/main
Date:   20.09.2023
Description: 
        Enhanced version of the dataset for image segmentation tasks
        
        - Multiple objects possible in one picture
        - Masks are generated accordingly - circle 3, rectangle 2, triangle 1, 
        where objects are present

If you use this code, please cite my name and GitHub
"""

import cv2
import numpy as np
import os
import random
import matplotlib.pyplot as plt

# Params which have to be set
NUM_IMAGES = 5000
IMG_SIZE = 128
STORAGE_PATH = 'C:\\Users\\IBM\\GIT_Hub\\ai-dev\\70-Segmentation\\dataset'

# Create folders for shapes, images, and masks
shapes = ["triangle", "rectangle", "circle"]

#for shape_folder in shapes:
os.makedirs(os.path.join(STORAGE_PATH, f"images/"), exist_ok=True)
os.makedirs(os.path.join(STORAGE_PATH, f"masks/"), exist_ok=True)

# Which objects we want to generate in one image
def generate_img_obj(shapes):
    # Amount of object classes to be generated
    OBJ_NUM = random.randint(1, len(shapes)) # minimum 1 object, maximum 3 objects
        
    obj_ids_lst = []
    for _ in range(0, OBJ_NUM):
        obj_ids_lst.append(random.randint(0, 2)) # generate random int in interval [0..2] (all included)
        
    return obj_ids_lst

# Function to generate a random filled triangle
def generate_triangle(img, size, color):   
    p1 = (random.randint(10, size - 10), random.randint(10, size - 10))
    p2 = (random.randint(10, size - 10), random.randint(10, size - 10))
    p3 = (random.randint(10, size - 10), random.randint(10, size - 10))
    triangle_cnt = np.array([p1, p2, p3])
    cv2.drawContours(img, [triangle_cnt], 0, color, thickness=cv2.FILLED)
    return img

# Function to generate a random filled rectangle
def generate_rectangle(img, size, color): 
    x1 = random.randint(10, size - 50)
    y1 = random.randint(10, size - 50)
    x2 = x1 + random.randint(20, 40)
    y2 = y1 + random.randint(20, 40)
    cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness=cv2.FILLED)
    return img

# Function to generate a random filled circle
def generate_circle(img, size, color):
    '''
    img ... input image as uint8, e.g. np.zeros((size, size), dtype=np.uint8)
    size ... image dimension as a single number
    color ... object color in BGR
    '''
    center = (random.randint(20, size - 20), random.randint(20, size - 20))
    radius = random.randint(10, size//3)
    cv2.circle(img, center, radius, color, thickness=cv2.FILLED)
    return img

def create_mask(canvas, color, label):
    '''
    canvas ... which canvas/image
    color ... BGR tuple (B, G, R)
    label ... mask value for pixels which match color
    '''
    # Use color from the predefined list
    #col_np = np.array(color)
    #col_arr = col_np.reshape(1, -1)          
    #print('color', col_arr)
    old_canvas = canvas
    
    lower_bound = color
    upper_bound = color
    print('lower bound :', lower_bound, ', upper bound:', upper_bound)    
    
    mask = cv2.inRange(canvas, lower_bound, upper_bound)
    print(np.max(mask), np.min(mask))
    binary_mask = np.where(mask > 0, label, 0).astype(np.uint8)
    print(np.max(binary_mask), np.min(binary_mask))
    bitwise_mask = cv2.bitwise_and(canvas, canvas, mask=mask)
    print(np.max(bitwise_mask), np.min(bitwise_mask))
    
    return mask, binary_mask, bitwise_mask

def create_color_tuples(lst):
    '''
    lst ... list of objects to be generated
    '''
        
    # BGR unique colors
    color_lst = []
    i = 0    
    while len(color_lst)<len(lst):
        i += 1
        color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
        if color not in color_lst: 
            color_lst.append(color)
        else:
            color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
            if color not in color_lst: color_lst.append(color)
        
        #print('bgr', i, color)
        
    return color_lst

# Function to generate a random filled circle
def generate_objects(lst, size, color_lst):
    '''
    
    '''
    # Setup default variables
    img = np.zeros((size, size), dtype=np.uint8)
    mask = np.zeros((size, size), dtype=np.uint8)
    canvas = np.zeros((size, size), dtype=np.uint8)
    canvas = cv2.cvtColor(canvas, cv2.COLOR_GRAY2BGR)
    
    # Masks
    masks_lst = []
    
    # iterate through our randomly generated object list
    #print('===================')
    #print('colors', color_lst)
    #print('delka seznamu', len(color_lst))
    
    #print('for loop', lst)
    color_idx = 0
    for l in lst:
        #print(l)
        # Take color from the pre-generated list
        set_color = color_lst[color_idx]
        
        if shapes[l] == "circle": #3
            #print("circle")
            img = generate_circle(canvas, size, set_color)
            #mask, binary_mask, bitwise_mask = create_mask(canvas, set_color, 255)
            mask, binary_mask, bitwise_mask = create_mask(canvas, set_color, 3)
            masks_lst.append(binary_mask)
        
        if shapes[l] == "rectangle": #2
            #print("rectangle")
            img = generate_rectangle(canvas, size, set_color)
            #mask, binary_mask, bitwise_mask = create_mask(canvas, set_color, 150)
            mask, binary_mask, bitwise_mask = create_mask(canvas, set_color, 2)
            masks_lst.append(binary_mask)          
        
        if shapes[l] == "triangle": #1
            #print("triangle")
            img = generate_triangle(canvas, size, set_color)
            #mask, binary_mask, bitwise_mask = create_mask(canvas, set_color, 90)
            mask, binary_mask, bitwise_mask = create_mask(canvas, set_color, 1)
            masks_lst.append(binary_mask)
                    
        # Next color
        color_idx += 1       
            
    # Final original image w/ all the objects generated  
    img = canvas
    
    # Mask image
    #for iter, color in enumerate(color_lst):
    #    print(iter, color)
    
    # Get the final mask of all objects    
    #mask = binary_mask
    #print('shape', masks_lst)
    final_mask = masks_lst[0]
    
    if len(masks_lst)>1:
        
        for id, mask_iter in enumerate(masks_lst):
            if id == 0: continue
            #print('->', id, mask_iter)
            final_mask = np.where(masks_lst[id]>0, masks_lst[id], final_mask)
        pass
    
    # Pass th final mask
    mask = final_mask
               
    return img, mask
    
# Generate NUM_IMAGES amount of pictures with randomly generated objects
for i in range(NUM_IMAGES):
    #print('******************')
    print('start iteration', i)
    # Which objects to generate from the 'shapes' list 
    lst = generate_img_obj(shapes)
    #print('obj list',lst)
    
    # BGR unique color for every object in the picture
    color_lst = create_color_tuples(lst)
    
    # Generate objects
    img, mask = generate_objects(lst, IMG_SIZE, color_lst=color_lst)

    # Save original and mask
    image_filename = os.path.join(STORAGE_PATH, f"images/image_{i}.png")
    mask_filename = os.path.join(STORAGE_PATH, f"masks/mask_{i}.png")
    #print(image_filename)
    cv2.imwrite(image_filename, img)
    cv2.imwrite(mask_filename, mask)
    print('******************')
    #print('end iteration', i)
