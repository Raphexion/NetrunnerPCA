from imageio import *
from spaces import create_space
from functools import partial
from matplotlib import pylab
import pickle

# load images
all_images = get_images()
org_shape = all_images[0].shape
images = filter(lambda i: i.shape == org_shape, all_images)

# turn into points
points = map(image_to_point, images)

# calculuate and save eigenvectors
U, s, V = create_space(points)

with open('U.pickle', 'wb') as handle:
    pickle.dump(U, handle)
with open('s.pickle', 'wb') as handle:
    pickle.dump(s, handle)
with open('V.pickle', 'wb') as handle:
    pickle.dump(V, handle)

# save some images to illustrate a point
eigenimages = map(partial(point_to_image, org_shape), V)

for ii, ei in enumerate(eigenimages):
    ei.save('eigenimage_{:04d}.png'.format(ii))
