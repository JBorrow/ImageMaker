''' This class brings together almost all of the code written by me during my
time working with Richard Bower and others at the ICC in Durham on the EAGLE
project.

It is used to create images, videos etc.
'''

import os
import numpy as N
#class that holds all of the possible styles in a class
from ImageStyles import *
#richard's eagle class that contains the plotting code
import plot_eagle_image as eagle

class ImageObject:
  '''Use this class to initialise the object with properties, such as object
  number or position etc.'''
  
  #initialise variables used so we don't forget about them!
  
  self.objectNumber
  self.objectPosition
  
  self.nFof
  self.firstFof
  self.fofStep
  
  self.imageStyle
  self.width
  self.scale
  self.starScaleFactor
  self.darkScaleFactor
  self.tLimits
  self.xPixels
  self.yPixels
  self.useLogh
  self.useText
  self.angle
  self.gasCmap
  self.cameraZDistance
  self.perspective
  self.opacity
  self.rotating
  self.partplot
  
  self.imageParams
  self.plotParams
  
  def __init__(self, objectNumber = 0, objectPosition = N.array(0.,0.,0.),
  imageStyle = ImageStyles.xsmall, rotating=False,
  partplot = [True, True, True, True, True]):
    self.objectNumber = objectNumber
    self.objectPosition = objectPosition
    self.imageStyle = imageStyle
    self.rotating = rotating
    self.partplot = partplot
    
    self.imageStyleUnpack()
    
  def imageStyleUnpack(self):
    '''Takes the given imagestyle and returns the values stored within its
    dictionary to the values in the class'''
    self.width = self.imageStyle['width']
    self.scale = N.array(self.imageStyle['scale'])
    self.starScaleFactor = self.imageStyle['star_scale_factor']
    self.darkScaleFactor = self.imageStyle['dark_scale_factor']
    self.tLimits = N.array(self.imageStyle['T_limits'])
    
    if 'pixels' in self.imageStyle.keys(): #image resolution
      self.xPixels, self.yPixels = self.imageStyle['pixels']
    else:
      self.xPixels, self.yPixels = 1024, 1024

    if 'use_logh' in self.imageStyle.keys(): #don't know what this does
      self.useLogh = self.imageStyle['use_logh']
    else:
      self.useLogh = True

    if 'text' in self.imageStyle.keys(): # overlay text e.g. position
      self.useText = self.imageStyle['text']
    else:
      self.useText = True

    if 'angle' in self.imageStyle.keys():
      self.angle = self.imageStyle['angle']
    else:
      self.angle = 0

    if not self.gasCmap:
      self.gasCmap = self.imageStyle['gas_cmap'] #don't know what this does

    if 'camera_z_distance' in self.imageStyle.keys():
      #setting z distance and perspective plot
      self.cameraZDistance = self.imageStyle['camera_z_distance']
      self.perspective = True
    else:
      self.cameraZDistance = None
      self.perspective = False

    if 'opacity' in self.imageStyle.keys(): #set opacity of gas etc
      self.opacity = self.imageStyle['opacity']
    else:
      self.opacity = 0

    return True
      
  def paramPack(self):
    '''Packs up the data in the class into two subclasses, imageParams and
    plotParams.'''
    
    self.imageParams = eagle.ImageParams(self.width, self.scale, zoom = 1.,
    angle = self.angle, partpot = self.partplot,
    star_scale_factor = self.starScaleFactor,
    dark_scale_factor = self.darkScaleFactor, gas_cmap = self.gasCmap,
    T_limits = self.tLimits, use_logh = self.useLogh,
    perspective = self.perspective, camera_z_distance = self.cameraZDistance,
    opacity = self.opacity)

    self.plotParams = eagle.PlotParams(xpixels = xPixels, ypixels = yPixels,
    text = useText)

    return True
      
  def ensureDir(self, directory):
    '''Checks if a directory exists. If it doesn't, it creates it'''
    d = os.path.dirname(directory)
    
    if not os.path.isdir(d):
      os.makedirs(d)
      
    return True
  

