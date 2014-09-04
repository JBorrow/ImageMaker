'''
This class is used to create rotations of objects for EAGLE.

Inherits from ImageClass

Joshua Borrow                                                                   
28/07/2014                                                                      
Institute For Computataional Cosmology, Durham University                       
The EAGLE Project                                                               
joshua.borrow@durham.ac.uk
'''

from ImageStyles import * 
import ImageClass
import copy
from multiprocessing import Process

class Rotation(ImageClass.Image):
    '''Creates rotations around some point etc. tries to keep __init__
    minimal'''
	
    def __init__(self, partplot = [True, True, True, True, True],
    saveDir = "~", gasCmap = None):
        '''This is pretty much the exact same init as the class we inherit from.
        This is kept minimal so we can give the user as much flexibility as
        possible'''
		
	self.partplot = partplot
	self.saveDir = saveDir
	self.gasCmap = gasCmap
		
	return

    def makeObjectRotation(self, imageStyle = ImageStyles.xsmall,
    snapNumber = 28, objectNumber = 0, text = True, nFrames = 360, nCores = 4):
        '''This requires a number of frames and number of cores, which have
        defaults of 360 and 4 respecvitely. nFrames % nCores must be equal to 0
        otherwise we will have missed frames'''

	# first we get the 'baseData' which contains all the info for us to plot
        self.objectNumber = objectNumber
        self.snapNumber = snapNumber
        self.imageStyle = imageStyle

        self.imageStyleUnpack()
        #now we package
        self.paramPack()
        self.fileInfoPack(rotating = False)

        self.baseDataGrabber
        
        if nFrames % nCores != 0:
	    print "Sorry, you need to have nFrames % nCores == 0"
	    exit(-1)
		
        step = nFrames/nCores

        for startAngle in range(0, 360, step):
            jobs = []
            for angle in range(startAngle, startAngle + step):
                # we start some processes up for each angle and kill them after
                # to keep the memory useage low
                jobs.append(Process(target = self.makeImageFromBaseData,
                args = (angle)))

            for job in jobs:
                job.start()

            for job in jobs:
                job.join()

        return

    def makeImageFromBaseData(self, angle = 0):
        '''Uses self.baseData to create images of some given angle'''

        thisData = copy.deepcopy(self.baseData)

        thisData.ImageParams.angle = angle
        thisData.plot_image()

        thisData = None

        return

if __name__ == "__main__":
    rot = Rotation()
    rot.makeObjectRotation(objectNumber=1727)
