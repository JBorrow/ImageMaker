'''
This file contains the code to create rotations parallelised.
'''

from multiprocessing import Process
import rgbPlotterMethods as rgb
import NewRotation as NR

def makeRotation(sizeList, snapList, objectList, text=True, saveDir = "/cosma5/data/dp004/dc-gues3/test_images", nFrames=360, nCores=4):
    jobsList = []
    if nFrames % nCores == 0:
        nProcess = nFrames/nCores
        #set the save directory
        print "setting directory"
        fileDir = ("Webpage/Centre%2.2f_%2.2f_%2.2f/Snapshot\
                %2.0f/%s/rotation"%(centre[0], centre[1], centre[2], snap,
                size['name']))
        #make sure it exists, otherwise we die
        rgb.ensureDir(saveDir + fileDir)

        NR.rotationMaker(sizeList, snapList,
        objectList, text, nFrames, nCores,
        saveDir)

    else:
        print "nFrames and nCores not compatible. Sorry bro. Exiting..."
        exit(-1)


if __name__ == "__main__":
    print "you made it here at least"
    makeRotation([ImageStyles.xsmall], [28], [1827])
