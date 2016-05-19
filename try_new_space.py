from imageio import get_images, image_to_point, point_to_image
from spaces import transform
import pickle
import numpy as np


# load images
all_images = get_images()
org_shape = all_images[0].shape
images = filter(lambda i: i.shape == org_shape, all_images)

# turn into points
points = map(image_to_point, images)

# load up U, s, V

with open('U.pickle', 'rb') as handle:
    U = pickle.load(handle)

with open('s.pickle', 'rb') as handle:
    s = pickle.load(handle)

with open('V.pickle', 'rb') as handle:
    V = pickle.load(handle)

for depth in np.arange(0.2, 1.1, 0.2):
    for ii, point in enumerate(points):
        y = transform(s, V, point, depth)
        y_im = point_to_image(org_shape, y)
        y_im.save('tr_card_{:04d}_{:03d}.png'.format(ii, int(depth*100)))
