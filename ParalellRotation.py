'''
This file contains the code to create rotations parallelised.
'''

from multiprocessing import Process
import rgbPlotterMethods as rgb
import NewRotation as NR

def makeRotation(sizeList, snapList, objectList, text, saveDir, nFrames, nCores):
    jobsList = []
    if nFrames % nCores == 0:
        nProcess = nFrames/nCores
        #set the save directory
        fileDir = ("Webpage/Centre%2.2f_%2.2f_%2.2f/Snapshot\
                %2.0f/%s/rotation"%(centre[0], centre[1], centre[2], snap,
                size['name']))
        #make sure it exists, otherwise we die
        rgb.ensureDir(saveDir + fileDir)

        NR.rotationMaker(sizeList, snapList,
        objectList, text, nFrames, nCores,
        saveDir = "/cosma5/data/dp004/dc-gues3/test_images")

    else:
        print "nFrames and nCores not compatible. Sorry bro. Exiting..."
        exit(-1)
