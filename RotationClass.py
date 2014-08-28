'''
This class is used to create rotations of objects for EAGLE.

Inherits from ImageClass

Joshua Borrow                                                                   
28/07/2014                                                                      
Institute For Computataional Cosmology, Durham University                       
The EAGLE Project                                                               
joshua.borrow@durham.ac.uk
'''

import ImageClass
import copy
from multiprocessing import Process

class Rotation(ImageClass.Image):
  '''Creates rotations around some point etc. tries to keep __init__ minimal'''
  
  def __init__(self, partplot = [True, True, True, True, True], saveDir = "~",
  gasCmap = None):
    '''This is pretty much the exact same init as the class we inherit from.
    This is kept minimal so we can give the user as much flexibility as
    possible'''
    
    self.partplot = partplot
    self.saveDir = saveDir
    self.gasCmap = gasCmap
    
    return

  def makeObjectRotation(self, imageStyle = ImageStyles.xsmall, snapNumber = 28,
  objectNumber = 0, text = True, nFrames = 360, nCores = 4):
    '''This requires a number of frames and number of cores, which have defaults
    of 360 and 4 respecvitely. nFrames % nCores must be equal to 0 otherwise we
    will have missed frames'''

    if nFrames % nCores != 0:
      print "Sorry, you need to have nFrames % nCores == 0"
      exit(-1)
    
    step = nFrames/nCores

    jobs = []
    for core in range(step):
      jobs.append(Process(target = self.angleIterator,
      args = (objectNumber, snapNumber,imageStyle, nFrames, nCores, core)))
    
    for job in jobs:
      job.start()

    #so we don't miss frames
    for job in jobs:
      job.join()

    return
    
  def angleIterator(self, objectNumber, snapNumber, imageStyle, nFrames, nCores,
  thisCore):
    '''This function is used to iterate through the angles and create images
    at each point. It is a very basic function that will just call the
    makeObjectImage or makePosImage. This is semi inefficient as it reads
    each time, but this **SHOULD** reduce memory useage.'''

    for angle in range(thisCore, nFrames/nCores, nFrames):
      #We need to create instances of the object for every single angle
      #so that we don't mess up self variables

      thisAngle = ImageClass.Image(self.partplot, self.saveDir, self.gasCmap)
      thisAngle.makeObjectImage(objectNumber, snapNumber, imageStyle, angle)
      thisAngle = None

    return
