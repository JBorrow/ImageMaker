"""Small script that makes a rotation of the whole box evolving"""

import numpy
from RotationClass import *
from ImageStyles import *
from multiprocessing import Process


def make_image(snip, angle):
	# make me a rotation instance
	image_maker = Rotation(saveDir="/cosma/home/mphf18/Data/HugeRot",
						   subsample=10)

	image_maker.makePosImage(imageStyle=ImageStyles.wanhundrad,
								snapNumber=snip,
								position = numpy.array([0., 0., 0.]),
								angle=angle)
	return

for snip in reversed(range(406)):
	prc = Process(target=make_image, args=(snip, snip))
	prc.start()
	# only want 1 at once
	prc.join()