import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image

assets_dir = f"{os.getcwd()}/assets"
path_cb_18x18 = f"{assets_dir}/checkerboard_18x18.png"
path_cb_84x84 = f"{assets_dir}/checkerboard_84x84.jpeg"
path_coca = f"{assets_dir}/coca-cola-logo.png"

# print in black/white pixel values in 2d py array
cb_18x18_image = cv2.imread(path_cb_18x18, 0)
cb_84x84_image = cv2.imread(path_cb_84x84, 0)
coca_image = cv2.imread(path_coca, 1)

# print image attributes: size as (h,w)
# print(cb_18x18_image.shape)
# print(cb_84x84_image.shape)
print(coca_image.shape)

# display image using matplotlib
# plt.imshow(cb_84x84_image, cmap="gray")

# fix - matplot expects RGB, opencv expects BGR, reverse the color channels
coca_image_reverse_channels = coca_image[:, :, ::-1]
plt.imshow(coca_image_reverse_channels)

plt.show()
