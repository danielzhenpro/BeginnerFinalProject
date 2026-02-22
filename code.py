import imageio.v3 as iio

filenames = ['mrbeats1.png', 'mrbeats2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('mrbeats.gif', images, duration = 500, loop = 0)
