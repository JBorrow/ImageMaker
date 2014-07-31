'''
This acts as a command-line wrapper that makes movies using the
MovieMaker.py module.

-ci "<x> <y> <z>"              		initial centre?
-cf "<x> <y> <z>"			   		final centre?
-z "<initial redshift>"
-s "<sizename>"   			   		size?
-t <t/f>                       		text on image?
-sd "<Save directory>"         		save directory?
-da "<value>"				   		delta angle for rotating
-p "Gas, DM, Stars, Hi, BH" <t/f>   partplot?
-tag								tag your save as a string. REQUIRED.
'''

import sys
import numpy as N
from ImageStyles import *
import time
import MovieMaker as MM

args = sys.argv

da = 0
ci = N.array([0,0,0])
cf = N.array([0,0,0])
z = 10
sizeList = [ImageStyles.xsmall]
text = True
saveDir = "/cosma5/data/dp004/dc-gues3/test_images"
tag = False

#search through to find some args

#CENTRE LISTS

if "-ci" in args:
	index = args.index("-ci")
	ci = args[index+1]

	List = ci.split()
	floatlist = []
	for item in List:
		floatlist.append(float(item))

	initial = N.array(floatlist)

if "-cf" in args:
	index = args.index("-cf")
	cf = args[index+1]

	List = cf.split()
	floatlist = []
	for item in List:
		floatlist.append(float(item))

	final = N.array(floatlist)

#REDSHIFT?

if "-z" in args:
	index = args.index('-z')
	z = float(args[index+1])

#SIZE LIST?

if '-s' in args:
    index = args.index('-s')
    sl = args[index + 1]

    #we get this as a string, and we need to turn it back to a list

    List = sl.split()

    sizeList = []

    if 'xxsmall' in List:
        sizeList.append(ImageStyles.xxsmall)

    if 'xxsmall_2' in List:
        sizeList.append(ImageStyles.xxsmall_2)

    if 'xxsmall_gist' in List:
        sizeList.append(ImageStyles.xxsmall_gist)

    if 'xxsmall_linear' in List:
        sizeList.append(ImageStyles.xxsmall_linear)

    if 'xsmall' in List:
        sizeList.append(ImageStyles.xsmall)

    if 'small' in List:
        sizeList.append(ImageStyles.small)

    if 'medium_hi' in List:
        sizeList.append(ImageStyles.medium_hi)

    if 'medium' in List:
        sizeList.append(ImageStyles.medium)

    if 'medium_rotation' in List:
        sizeList.append(ImageStyles.medium_rotation)

    if 'large' in List:
        sizeList.append(ImageStyles.large)

    if 'xlarge' in List:
        sizeList.append(ImageStyles.xlarge)

    if 'xlarge_rotation' in List:
        sizeList.append(ImageStyles.xlarge_rotation)

    if 'xxlarge' in List:
        sizeList.append(ImageStyles.xxlarge)

    if 'exhibition' in List:
        sizeList.append(ImageStyles.exhibition)

    if 'exhibition2' in List:
        sizeList.append(ImageStyles.exhibition2)

    if 'exhibition_rotation' in List:
        sizeList.append(ImageStyles.exhibition_rotation)

    if 'supersize' in List:
        sizeList.append(ImageStyles.supersize)

    if 'supersize_rotation' in List:
        sizeList.append(ImageStyles.supersize_rotation)

    if 'supersize_simple' in List:
        sizeList.append(ImageStyles.supersize_simple)

    if 'custom' in List:
        sizeList.append(ImageStyles.custom)

    if 'app' in List:
        sizeList.append(ImageStyles.app)

    if 'long_shot' in List:
        sizeList.append(ImageStyles.long_shot)


if '-t' in args:
    index = args.index('-t')
    tf = args[index + 1]

    if tf == 't':
        text = True

    elif tf == 'f':
        text = False

    else:
        text = False

if '-sd' in args:
    index = args.index('-sd')

    saveDir = args[index + 1]

if "-da" in args:
	index = args.index('-da')
	da = float(args[index+1])

if '-p' in args:
    index = args.index('-p')

    tf = args[index + 1]

    plot = tf.split()
    partplot = []

    for i in range(5):
        if plot[i] == 't':
            partplot.append(True)
        else:
            partplot.append(False)

if '-tag' in args:
	index = args.index('-tag')

	tag = args[index+1]


sizeListPrinter = []

for size in sizeList:
    sizeListPrinter.append(size['name'])

print "Initial: ", initial
print "Final: ", final
print "Initial redshift", z
print "sizeList: ", sizeListPrinter
print "Text: ", text
print "saveDir: ", saveDir
print "Delta angle: ", da

if not tag:
	print "No tag specified. Cannot continue"
	exit(-1)

time.sleep(10)

print "Calling the makeSingleMovie function"

MM.makeSingleMovie(initial, final, z, sizeList[0], text, saveDir, da,
				  tag, partplot)
