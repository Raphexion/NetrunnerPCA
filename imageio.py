import os
from PIL import Image
import matplotlib.image as mpimg
import numpy as np

def _get_image_filenames(folder):
    images=[]
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(('.png',)):
                images.append(os.path.join(root, file))
    return images

def get_images(folder='images/'):
    """
    Some images have alpha channels, some don't.
    Make sure to only keep RGB, by using [:, :, 0:3]
    """
    filenames = _get_image_filenames(folder)
    org_images = [mpimg.imread(fn) for fn in filenames]
    rgb_images = [im[:, :, 0:3] for im in org_images]
    return rgb_images

def image_to_point(image):
    return np.array(image.ravel(), dtype=np.float32)

def point_to_image(org_shape, point_):
    point = point_.copy().reshape(org_shape)

    min_val = point.min()
    max_val = point.max()
    point = (point - min_val) * 255 / (max_val - min_val)

    return Image.fromarray(np.uint8(point))
