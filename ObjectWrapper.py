'''
This acts as a command-line wrapper that makes images and rotations using the
rgbPlotterMethods module.

-r <t/f>                       rotating?
-sn "<snap1> <snap2> <...>"    snaps?
-sl "<size1> <size2> <...>"    sizes?
-ol "<obj1> <obj2> <...>"      objects?
-t <t/f>                       text on image?
-sd "<Save directory>"         save directory?
-p <t/f>                       parallelise?

It checks if less than 25 cores are going to be used and if greater asks the
user to use the queue system.
'''

import sys
import numpy as N
from ImageStyles import *
import time
from multiprocessing import Process
import rgbPlotterMethods as rgb
import ParalellRotation as para

args = sys.argv

rotating=False
snapList = [28]
objectList = [1172]
sizeList = [ImageStyles.xsmall]
text = True
saveDir = "/cosma5/data/dp004/dc-gues3/test_images"
parallelise = True

#search through to find some args
#ROTATING?
if '-r' in args:
    index = args.index('-r')
    tf = args[index + 1]

    if tf == 't':
        rotating = True

    elif tf == 'f':
        rotating = False

    else:
        rotating = False


#SNAP LIST LIST?
if '-sn' in args:
    index = args.index('-sn')
    sn = args[index + 1]

    #we get this as a string, we need to turn it back into a list

    List = sn.split()
    snapList = []
    #now to convert to integers...

    for string in List:
        snapList.append(int(string))



#SIZE LIST?

if '-sl' in args:
    index = args.index('-sl')
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
        
    if 'joshrot' in List:
        sizeList.append(ImageStyles.joshrot)

    if 'large' in List:
        sizeList.append(ImageStyles.large)

    if 'xlarge' in List:
        sizeList.append(ImageStyles.xlarge)

    if 'xlarge_rotation' in List:
        sizeList.append(ImageStyles.xlarge_rotation)
        
    if 'xlarge_hr' in List:
        sizeList.append(ImageStyles.xlarge_hr)

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



#OBJECT LIST?
if '-ol' in args:
    index = args.index('-ol')
    ol = args[index + 1]

    #we get this as a string, we need to turn it back into a list

    List = ol.split()
    objectList = []
    #now to convert to integers...

    for string in List:
        objectList.append(int(string))

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

if '-p' in args:
    index = args.index('-p')

    tf = args[index + 1]

    if tf == 't':
        parallelise = True

    elif tf == 'f':
        parallelise = False

    else:
        parallelise = True


sizeListPrinter = []

for size in sizeList:
    sizeListPrinter.append(size['name'])

print "Rotating: ", rotating
print "snapList: ", snapList
print "objectList: ", objectList
print "sizeList: ", sizeListPrinter
print "Text: ", text
print "saveDir: ", saveDir
print "Parallelise: ", parallelise

#now we'll perform some checks!

for snap in snapList:
    if snap not in range(29):
        print "Snap not in range 0 - 28, exiting..."
        exit(-1)

    if snapList.count(snap) > 1:
        print "Snap entered twice, exiting..."
        exit(-1)

for number in objectList:
    if number not in range(2000):
        print "Object not in range 0 - 2000, exiting..."
        exit(-1)

    if objectList.count(number) > 1:
        print "Object entered twice, exiting..."
        exit(-1)


print "Looks okay to me! Calling the makeObjectImages function!"

if rotating:
    para.makeRotation(sizeList, snapList, objectList, text, saveDir, 360, 4)

else:
    rgb.makeObjectImages(rotating, sizeList, snapList, objectList, text, saveDir)
