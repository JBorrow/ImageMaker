'''
This file contains the code to create rotations parallelised.
'''

from multiprocessing import Process
import rgbPlotterMethods as rgb
import NewRotation as NR

def makeRotation(sizeList, snapList, objectList, text=True, saveDir = "/cosma5/data/dp004/dc-gues3/test_images", nFrames=360, nCores=4, partplot=[True, True, True, True, True]):
    jobsList = []
    if nFrames % nCores == 0:
        nProcess = nFrames/nCores
        #set the save directory
        print "setting directory"
        fileDir = ("Webpage/Object%4.4i/Snapshot\
                %2.0f/%s/rotation"%(objectList[0],snapList[0],
                sizeList[0]['name']))

        NR.rotationMaker(sizeList, snapList,
        objectList, text, nFrames, nCores,
        saveDir, partplot)

    else:
        print "nFrames and nCores not compatible. Sorry. Exiting..."
        exit(-1)


if __name__ == "__main__":
    print "you made it here at least"
    makeRotation([ImageStyles.xsmall], [28], [1827])
