'''

These files are meant to replace make_standard_images.py as it is an
uncommented, unmodular mess (sorry Richard...)

This file contains the functions that call from the Eagle image creations to
give us more flexibility.

Josh Borrow
Durham University
Institute for Computational Cosmology
07/07/2014
'''

from ImageStyles import *

import plot_eagle_image as eagle
import sys
import numpy as N
import time
import pylab as P
import os
import fnmatch

#make sure you're eagle

os.system("newgrp dp004-eagle")
os.system("umask 002")


def ensureDir(directory):
    d = os.path.dirname(directory)

    if not os.path.exists(d):
        os.system("mkdir -p " + str(d))

def fofGallery(fileInfo, style=ImageStyles.xsmall, nfof=1, first_fof=1,
    fof_step=1, gasCmap=None, partplot = [True, True, True, True, False]):
    '''
    This makes an image with a scaling suitable for looking at an individual
    galaxy. Object 1 is the first halo, and this method doesn't work for
    Object 0.

    We assume that the large image should be gas + stars.

    This method requires the help of others to get the 'fileInfo section'
    '''

    #declare some basic variables used in creating the image
    width = style['width']
    scale = N.array(style['scale'])
    starScaleFactor = style['star_scale_factor']
    darkScaleFactor = style['dark_scale_factor']
    TLimits = N.array(style['T_limits'])

    if 'pixels' in style.keys(): #image resolution
        xPixels, yPixels = style['pixels']

    else:
        xPixels, yPixels = 1024, 1024


    if 'use_logh' in style.keys(): #don't know what this does
        useLogh = style['use_logh']

    else:
        useLogh = True


    if 'text' in style.keys(): # overlay text e.g. position
        useText = style['text']

    else:
        useText = True


    if 'angle' in style.keys():
        angle = style['angle']

    else:
        angle = 0


    if not gasCmap:
        gasCmap = style['gas_cmap'] #don't know what this does


    if 'camera_z_distance' in style.keys():
        #setting z distance and perspective plot
        cameraZDistance = style['camera_z_distance']
        perspective = True

    else:
        cameraZDistance = None
        perspective = False


    if 'opacity' in style.keys(): #set opacity of gas etc
        opacity = style['opacity']

    else:
        opacity = 0




    #now give these params to the eagle function

    imageParams = eagle.ImageParams(width, scale, zoom=1., angle=angle,
    partplot=partplot, star_scale_factor = starScaleFactor,
    dark_scale_factor = darkScaleFactor, gas_cmap = gasCmap,
    T_limits = TLimits, use_logh = useLogh, perspective = perspective,
    camera_z_distance = cameraZDistance, opacity = opacity)

    plotParams = eagle.PlotParams(xpixels = xPixels, ypixels = yPixels,
    text = useText)


    #now we make the images

    if not fileInfo.rotating:
        print " Making fof images for halos", first_fof, "to" ,
        first_fof + nfof - 1

        eagle.make_gallery(fileInfo, imageParams, plotParams, nfof=nfof,
        first_fof = first_fof, fof_step = fof_step)

    else:
        print "Making fof images - rotation for halos", first_fof, "to",
        first_fof + nfof - 1

        for someFof in range(first_fof, first_fof+nfof):
            eagle.make_rotation(fileInfo, imageParams, plotParams,
            centre_fof=someFof)

    return


def imageAtPosition(fileInfo, style=ImageStyles.xsmall, centre = [0.,0.,0.],
    gasCmap = None, deltaAngle = 2., text=True,
    partplot = [True, True, True, True, False]):
    '''
    Make an image at some given position. Similar to above, except can be
    rotating.
    '''

    # declare variables from style

    width = style['width']
    scale = N.array(style['scale'])
    starScaleFactor = style['star_scale_factor']
    darkScaleFactor = style['dark_scale_factor']
    TLimits = N.array(style['T_limits'])


    if 'pixels' in style.keys(): #image resolution
        xPixels, yPixels = style['pixels']

    else:
        xPixels, yPixels = 1024, 1024


    if 'use_logh' in style.keys(): #don't know what this does
        useLogh = style['use_logh']

    else:
        useLogh = True


    if 'text' in style.keys(): # overlay text e.g. position
        useText = style['text']

    else:
        useText = True


    if 'angle' in style.keys():
        angle = style['angle']

    else:
        angle = 0


    if not gasCmap:
        gasCmap = style['gas_cmap'] #don't know what this does


    if 'camera_z_distance' in style.keys():
        #setting z distance and perspective plot
        cameraZDistance = style['camera_z_distance']
        perspective = True

    else:
        cameraZDistance = None
        perspective = False


    if 'opacity' in style.keys(): #set opacity of gas etc
        opacity = style['opacity']

    else:
        opacity = 0




    #now give these params to the eagle function

    imageParams = eagle.ImageParams(width, scale, zoom=1., angle=angle,
    partplot=partplot, star_scale_factor = starScaleFactor,
    dark_scale_factor = darkScaleFactor, gas_cmap = gasCmap,
    T_limits = TLimits, use_logh = useLogh, perspective = perspective,
    camera_z_distance = cameraZDistance, opacity = opacity)

    plotParams = eagle.PlotParams(xpixels = xPixels, ypixels = yPixels,
    text = useText)


    #we need to get the data from eagle

    #these extra params allow only a small subset to be found...

    baseData = eagle.eagle_image_data(fileInfo, imageParams, plotParams)
    baseData.ReadGroupData(surpress=False, centre=centre)

    if not fileInfo.rotating:
        print "Making images for position: ", centre
        eagle.make_single_image(baseData)

    else:
        print "Making fof images - rotation for position: ", centre
        #generate original image...
        data = eagle.make_single_image(baseData)
        #now make all the cool images around the position
        for angle in N.arange(delta_angle,360., delta_angle):
            baseData.imageParams.angle = angle
            eagle.make_single_image(baseData, mydata=data)

    return


def makeObjectImages(rotating=False, sizeList = [ImageStyles.xsmall],
    snapList = [28], objectList = [1172], text = True,
    saveDir = "/cosma5/data/dp004/dc-gues3/test_images"):
    '''
    Makes a set of images for the standard object numbers (0-9999). Creates
    in a directory /Webpage/<Object Number, Centre co-ords, Gallery>
    /Snapshot<snapshotnumber>/<size>
    '''

    #set up directories
    dir = "."

    #create and save images

    for size in sizeList:
        for snap in snapList:
            for object in objectList:
                #more directory setting up
                fileDir = ("/Webpage/Object%.0f/Snapshot%2.0f/%s"%(object,
                snap, size['name']))

                if rotating:
                    #save in a subdirectory called rotating
                    fileDir += "/rotation"

                #now we get the file info for each object
                fileInfo = eagle.FileInfo(dir, snap, "",saveDir + fileDir,
                rotating = rotating)

                #and finally complete the image
                ensureDir(saveDir + fileDir)

                fofGallery(fileInfo, size, first_fof = object, nfof=1)

    return


def makeImagesAtPosition(rotating = False, text = True, sizeList =
    [ImageStyles.xsmall], snapList = [28], centreList =
    [[0.,0.,0.]], saveDir = "/cosma5/data/dp004/dc-gues3/test_images"):
    '''
    Works the same as above however takes an argument of a list of lists
    unlike than the original. Also accepts a single list rather than
    a list and converts it if neccessary.
    '''

    #conversion to list type
    if type(centreList) != type([]):
        centreList = [centreList]

    #directory setup
    dir = "."

    #actual work
    for size in sizeList:
        for snap in snapList:
            for centre in centreList:
                fileDir = ("Webpage/Centre%2.2f_%2.2f_%2.2f/Snapshot\
                %2.0f/%s"%(centre[0], centre[1], centre[2], snap,
                size['name']))

                if rotating:
                    fileDir = fileDir + "/rotation"


                ensureDir(saveDir + fileDir)

                fileInfo = eagle.FileInfo(dir, snap, "", saveDir + fileDir,
                rotating = rotating, text = text)

                #create the image
                imageAtPosition(fileInfo, size, centre = centre,
                text = text)

    return


def makeObjectGallery(text = True, sizeList = [ImageStyles.xsmall],
    snapList = [28], nfof = 50, deleteFiles = True, first_fof = 0,
    fof_step = 1, subsample = 1,
    saveDir = "/cosma5/data/dp004/dc-gues3/test_images"):
    '''
    Makes a 'gallery' of images from the list of sizes of the first nfof
    objects. So normally this would start at object 0 and make images
    from 0 - 50.
    '''

    #directory setup
    dir = "."


    for size in sizeList:
        for snap in snapList:
            fileDir = ("/Webpage/Gallery/Snapshot%2.0f/%s"%(snap,
            size['name']))

            ensureDir(saveDir + fileDir)

            fileInfo = eagle.FileInfo(dir, snap, "", saveDir+fileDir,
            rotating=False)

            #create images
            fofGallery(fileInfo, size, nfof, first_fof,
            fof_step = fof_step)

            #cleanup
            os.system("cd " + fileInfo.savedir + " ; make_montage.csh")

            if deletefiles:
                os.system('rm -r '+ fileInfo.savedir + "/Object*")


    return

if __name__ == "__main__":
    makeObjectImages(objectList=[1821])
