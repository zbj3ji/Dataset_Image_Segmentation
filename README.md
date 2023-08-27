# Simple data set for image segmentation tasks

I was searching for a simple dataset where I could have an object and its corresponding mask (white for object present, black for object not present). I found nothing that met my expectations, so I created this simple script to generate three different objects - triangles, rectangles, and circles. They are generated in random colors and positions on the canvas, and the corresponding masks are also generated. You can run the Python script on your local machine or download some samples I've created and stored in the '[shapes](shapes)' folder.

**Please, don't forget to change following parameters before running the script on your local machine:**

```python
NUM_IMAGES = 15
STORAGE_PATH = 'E:\\data_sets\\shapes\\'
```
Here are a couple of examples of original/mask pairs:

![triangle_original1](shapes/images/triangle/triangle_image_0.png) ![triangle_mask1](shapes/masks/triangle/triangle_mask_0.png)
![triangle_original2](shapes/images/triangle/triangle_image_1.png) ![triangle_mask2](shapes/masks/triangle/triangle_mask_1.png)

![circle_original1](shapes/images/circle/circle_image_0.png) ![circle_mask1](shapes/masks/circle/circle_mask_0.png)
![circle_original2](shapes/images/circle/circle_image_1.png) ![circle_mask2](shapes/masks/circle/circle_mask_1.png)

![rectangle_original1](shapes/images/rectangle/rectangle_image_0.png) ![rectangle_mask1](shapes/masks/rectangle/rectangle_mask_0.png)
![rectangle_original2](shapes/images/rectangle/rectangle_image_1.png) ![rectangle_mask2](shapes/masks/rectangle/rectangle_mask_1.png)

If you use this code to generate your own data, please remember to cite this source as ![Dataset_Image_Segmentation](https://github.com/zbj3ji/Dataset_Image_Segmentation). Thank you!
