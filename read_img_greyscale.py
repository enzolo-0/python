import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image

assets_dir = f"{os.getcwd()}/assets"
path_cb_18x18 = f"{assets_dir}/checkerboard_18x18.png"
path_cb_84x84 = f"{assets_dir}/checkerboard_84x84.jpeg"

# print in black/white pixel values in 2d py array
cb_18x18_image = cv2.imread(path_cb_18x18, 0)
cb_84x84_image = cv2.imread(path_cb_84x84, 0)
print(cb_84x84_image)

