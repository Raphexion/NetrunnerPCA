from imageio import get_images, image_to_point, point_to_image
from spaces import create_space
from functools import partial
import pickle
from settings import eigen_folder
import os

if not os.path.exists(eigen_folder):
    os.makedirs(eigen_folder)

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
    fn = 'eigenimage_{:04d}.png'.format(ii)
    lc = os.path.join(eigen_folder, fn)
    ei.save(lc)
