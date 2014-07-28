'''
This program aims to create rotating images of objects with considerably lower
memory useage and higher CPU utlisation than one in plot_eagle_image.py.

In theory it only needs to read ONCE.

Josh Borrow
Durham University
Institute for Computational Cosmology
14/07/2014
'''

import plot_eagle_image as eagle
from ImageStyles import *
import os
from multiprocessing import Process
import copy
import gc

def ensureDir(directory):
    d = os.path.dirname(directory)

    if not os.path.exists(d):
        os.system("mkdir -p " + str(d))

def paramMaker(style = ImageStyles.xsmall, gasCmap = None,
    partplot = [True, True, True, True, True]):
    '''
    This funtion populates some imageParams and plotParams variables with the
    given values from the style etc.
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

    return imageParams, plotParams



def imageMaker(baseData, particleData, imageParams, nFrames = 360, nCores = 4):
    '''
    Makes the frames.
    '''

    step = 360*nCores/nFrames

    jobs = []
    for core in range(nCores):
        p = Process(target=angleIterator, args = (core, 360, step, baseData))
        jobs.append(p)
        jobs[core].start()

    for job in range(len(jobs)):
        jobs[job].join()


def angleIterator(start = 0, stop = 360, step = 1, baseData = None):
    '''
    This iterates through angles and makes images so we can use the
    multiprocessing module
    '''
    bD = copy.deepcopy(baseData)

    for angle in range(start, stop, step):
        baseData.imageParams.angle = angle

        baseData.plot_image(perspective=baseData.imageParams.perspective,
        camera_z_distance=baseData.imageParams.camera_z_distance,
        opacity=baseData.imageParams.opacity)
        baseData = None
        gc.collect()
        baseData = copy.deepcopy(bD)




def rotationMaker(sizeList = [ImageStyles.xsmall], snapList = [28],
    objectList = [0], text = True, nFrames = 360, nCores = 4,
    saveDir = "/cosma5/data/dp004/dc-gues3/test_images",
    partplot = [True, True, True, True, True]):
    '''
    The actual function. It will create the images in the given directory, and
    then will convert them into a movie file with 24fps and the same resolution
    as the images.

    It uses .h264 encoding, through mencoder.
    '''

    #create and save images

    for size in sizeList:
        for snap in snapList:
            for object in objectList:
                Dir = (saveDir + "/Webpage/Object%.0f/Snapshot%2.0f/%s/rotation"
                %(object, snap, size['name']))

                ensureDir(Dir)

                #let's read a subset of the data

                fileInfo = eagle.FileInfo(".", snap, "", Dir, rotating = True)

                imageParams, plotParams = paramMaker(size, partplot=partplot)

                baseData = eagle.eagle_image_data(fileInfo, imageParams,
                                                    plotParams)

                #now we read the data

                baseData.ReadGroupData(suppress=False, centre_fof=object)

                particleData = baseData.ReadParticleData(object)


                #now we need to call the function that actually makes the images

                imageMaker(baseData, particleData, imageParams, nFrames, nCores)
