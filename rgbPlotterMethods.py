'''

These files are meant to replace make_standard_images.py as it is an
uncommented, unmodular mess (sorry Richard...)

This file contains the methods that call from the Eagle image creations to give
us more flexibility.

Josh Borrow
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

class PlotterMethods:
    def __init__(self):
        return

    def fofGallery(fileInfo, style=ImageStyles.xsmall, nfof=1, first_fof=1,
        fof_step=1, gasCmap=None):
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

        imageParams = eagle.ImageParams(width, scale, zoom=1., angle,
        partplot=partplot, star_scale_factor = starScaleFactor,
        dark_scale_factor = darkScaleFactor, gas_cmap = gasCmap,
        T_limits = TLimits, use_logh = useLogh, perspective = perspective,
        camera_z_distance = cameraZDistance, opacity = opacity)

        plotParams = eagle.PlotParams(xpixels = xPixels, ypixels = yPixels,
        text = useText)


        #now we make the images

        if not fileInfo.rotating:
            print " Making fof images for halos", first_fof, to ,
            first_fof + nfof - 1

            eagle.make_gallery(fileInfo, imageParams, plotParams, nfof=nfof,
            first_fof = first_fof, fof_step = fof_step)

        else:
            print "Making fof images - rotation for halos", first_fof, "to",
            first_fof + nfof - 1

            for someFof in range(first_fof, first_fof+nfof):
                eagle.make_rotation(fileInfo, imageParams, plotParams,
                centre_fof=my_fof)


    def image_at_position():