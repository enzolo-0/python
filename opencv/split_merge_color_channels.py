import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image

assets_dir = f"{os.getcwd()}/assets"
path_lake = f"{assets_dir}/lake.png"

# split the image into BGR components
bgr_image = cv2.imread(path_lake, cv2.IMREAD_COLOR)
b, g, r = cv2.split(bgr_image)

# Show the Channels
plt.figure(figsize=([20, 5]))
plt.subplot(141);plt.imshow(r, cmap="gray"); plt.title("Red Channel")
plt.subplot(142); plt.imshow(g, cmap="gray"); plt.title("Green Channel")
plt.subplot(143); plt.imshow(b, cmap="gray"); plt.title("Blue Channel")

# Merge the individual channels into BGR image
merged_image = cv2.merge((b, g, r))
plt.subplot(144)
plt.imshow(merged_image[:, :, ::-1])
plt.title("Merged Output")

plt.show()
