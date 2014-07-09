'''
This class contains the code that is used to make a 'special gallery'.

A special gallery is one where there is a supersize (100 x 100 x 20 MPc) image
behind and smaller (100 Kpc) images laid on top, with arrows pointing to the
places on the large image where the smaller images can be found.

In previous versions, which were coded by Richard Bower, there were far too
many galxies trying to be overlaid on top of the supersize image and as such
there was no way of seeing them all. It really looked like a mess.

This version hopes to rectify this by limiting the number of 'xsmall' images of
galaxies laid on top to 6. (This number was chosen arbitarily, just because it
'seemed right'... How unscientific...)

Josh Borrow
Durham University
Institute for Computational Cosmology
08/07/2014
'''

from ImageStyles import *
from rgbPlotterMethods import *

#import plot_eagle_image as eagle
import sys
import numpy as N
import time
import pylab as P
import os
import fnmatch


def specialGallery(nfof, centre_fof = 0, fof_step = 1, first_fof = 0,
    remake_gallery = False, minitype = 'gas', label_only = False,
    subsample = 1, snapList = [28],
    largeStyle = ImageStyles.supersize_simple,
    smallStyle = ImageStyles.xsmall, saveDir = "./test_images"):
    '''
    This function is used to create the image. It will also check if the small
    images have been created already and if they have not it will create them.
    However, if remake_gallery = True, it will remake all of the images
    (this can be very time consuming, so use at your own peril.)

    Currently only one snapshot works for the snaplist, however you can
    iterate this with a simple script.
    '''

    #directory setup
    dir = "."
    filedir = ("/Webpage/Gallery/Snapshot%2.0f/%s" %(snapList[0],
                    largeStyle))

    #rename original centre fof
    fofForImage = centre_fof

    #check which objects are in the image - need to read the data
    #first we check what size we want the large image to be:

    width = largeStyle['width']
    scale = N.array(largeStyle['scale'])
    star_scale_factor = largeStyle['star_scale_factor']
    dark_scale_factor = largeStyle['dark_scale_factor']
    TLimits = N.array(largeStyle['T_limits'])

    if 'pixels' in largeStyle.keys():
        xPixels, yPixels = largeStyle['pixels']

    else:
        xPixels, yPixels = 1024, 1024


    if 'use_logh' in largeStyle.keys():
        use_logh = largeStyle['use_logh']

    else:
        use_logh = True


    #now we set parameters so we can read data

    fileInfo = eagle.FileInfo(dir, snapList[0], "", savedir+filedir,
    rotating = False)

    imageParams = eagle.ImageParams(width, scale, zoom = 1., angle = 0,
    partplot = [True, False, False],
    star_scale_factor = star_scale_factor,
    dark_scale_factor = dark_scale_factor, T_limits = TLimits,
    use_logh = use_logh, subsample = subsample)

    plotParams = eagle.PlotParams(xpixels = xPixels, ypixels = yPixels,
    text = True)

    #now we read some data

    print "Reading Data! Using ReadGroupData from Eagle!"

    baseData = eagle.eagle_image_data(fileInfo, imageParams, plotParams)
    baseData.ReadGroupData(suppress = False, centre_fof = 0)
    data = baseData.ReadParticleData(fofForImage)

    #okay, now we can actually see which of the objects are in the picture

    centre_fof_list = []

    print "Iterating to find object numbers!"

    for someFof in range(first_fof, nfof, fof_step):
        #this next line checks and leaves a border around the edge
        if not N.any(N.mod(N.abs(baseData.fof_centre[someFof]
        - baseData.fof_centre[fofForImage]), baseData.boxsize)
        > 0.7*N.array([0.3,0.3,0.5])*baseData.imageParams.width):
            print "Appending: ", someFof,
            centre_fof_list.append(someFof)

    centre_fof_list.sort()
    print "The objects in this image are: ", centre_fof_list

    #now we will select the ones we want. We'll take two big two middle and
    #two that are really small. Because we use int division,
    #floats are not a matter

    cFofLL = len(centre_fof_list)

    listOfObjects= [centre_fof_list[0], centre_fof_list[1],
    centre_fof_list[-1], centre_fof_list[-2],
    centre_fof_list[int(cFofLL/2) + 1], centre_fof_list[int(cFofLL/2) - 1]]

    print "The objects we're going to use are: ", listOfObjects

    #now let's check if they exist, and if they don't, we'll make them -
    #unless we've been told not to - in which case we won't.

    if not label_only:
        for someFof in listOfObjects:
            directory = "./test_images/Webpage/Gallery/Snapshot%2.0f/%s\
            /Object%4.4i" % (snapList[0], smallStyle['name'], someFof)
            if not remake_gallery:
                if os.path.isfile(directory)
                    continue
                else:
                    print "Creating an image of Object ", someFof, "!"
                    #set some info
                    littleInfo = eagle.FileInfo(dir, snapList[0], "", directory,
                    rotating = False)
                    #create the image and save it in the 'directory'
                    fofGallery(littleInfo, smallStyle, first_fof = someFof)

            else:
                print "Creating an image of Object ", someFof, "!"
                #set some info
                littleInfo = eagle.FileInfo(dir, snapList[0], "", directory,
                rotating = False)
                #create the image
                fofGallery(littleInfo, smallStyle, first_fof = someFof)



    print "Now creating the big image!"

    #create directory
    os.system("mkdir -p " + baseData.fileInfo.savedir)
    #create the 'plot'
    ax = baseData.plot_image(close_figure=False)


    #now we'd better get some cool stuff put on top of this big image...
    print "Adding images on top!"

    from matplotlib._png import read_png
    from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
    AnnotationBbox)

    for i in range(len(listOfObjects)):
        #find the file
        directory = "./test_images/Webpage/Gallery/Snapshot%2.0f/%s\
        /Object%4.4i" % (snapList[0], smallStyle['name'], someFof)

        #now we try to find the file and sort stuff out
        try:
            if minitype == 'gas':
                filename = directory + "/" + fnmatch.filter( os.listdir(mydir),
                "gas_image*" )[0]

            elif minitype == 'star':
                filename = directory + "/" + fnmatch.filter( os.listdir(mydir),
                "star_image*" )[0]

            else:
                filename = directory + "/" + fnmatch.filter( os.listdir(mydir),
                "phase_image*" )[0]

        except IndexError:
            print "The %s image does not exist for Object%4.4i"
            % (smallStyle['name'], listOfObjects[i])
            continue #nothing we can do, just try to keep going




    return

if __name__ == "__main__":
    specialGallery(100)
