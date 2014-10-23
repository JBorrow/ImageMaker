''' This class brings together almost all of the code written by me during my
time working with Richard Bower and others at the ICC in Durham on the EAGLE
project.

This class is used to create images of a given object or given position.
That is all. Making rotations, etc. is handled by other classes.

Joshua Borrow
24/07/2014
Institute For Computataional Cosmology, Durham University
The EAGLE Project
joshua.borrow@durham.ac.uk
'''

import os
import numpy as N
#class that holds all of the possible styles in a class
from ImageStyles import *
#richard's eagle class that contains the plotting code
import plot_eagle_image as eagle

class Image(object):
	'''Use this class to initialise the object with properties, such as object
	number or position etc.'''
 
	def __init__(self, partplot = [True, True, True, True, True],
	saveDir = "/cosma/home/mphf18/Data/test_images", gasCmap = None):
		'''We want to minise on the amount of things given to the init so that
		we can have maximum flexibility. I think these two are fair as they are
		unlikely to be changed during a script'''
		self.partplot = partplot
		self.saveDir = saveDir
		self.gasCmap = gasCmap
	
		return
		
	def imageStyleUnpack(self):
		'''Takes the given imagestyle and returns the values stored within its
		dictionary to the values in the class'''
		self.size = self.imageStyle['name']
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

		return
				
	def paramPack(self):
		'''Packs up the data in the class into two subclasses, imageParams and
		plotParams.'''
		
		self.imageParams = eagle.ImageParams(self.width, self.scale, zoom = 1.,
		angle = self.angle, partplot = self.partplot,
		star_scale_factor = self.starScaleFactor,
		dark_scale_factor = self.darkScaleFactor, gas_cmap = self.gasCmap,
		T_limits = self.tLimits, use_logh = self.useLogh,
		perspective = self.perspective,
		camera_z_distance = self.cameraZDistance,
		opacity = self.opacity)

		self.plotParams = eagle.PlotParams(xpixels = self.xPixels, 
		ypixels = self.yPixels, text = self.useText)

		return

	def fileInfoPack(self, rotating = False):
		'''Packages data in the class to the fileInfo object within the eagle
		class so that we can give it the data we need to put the files where it
		should'''
		
		try:
			self.totalDir = (self.saveDir +
			"/Webpage/Object%0.f/Snapshot%2.0f/%s/"
			% (self.objectNumber, self.snapNumber, self.size))
		except AttributeError:
			#catch the case where we have a position not an object defined
			self.totalDir = (self.saveDir + "/Webpage/Centre%3.2f_%3.2f_%3.2f/\
			Snapshot%2.0f/%s/" % (self.position[0], self.position[1],
			self.position[2], self.snapNumber, self.size))

		self.ensureDir(self.totalDir)

		self.fileInfo = eagle.FileInfo(".", self.snapNumber, "", self.totalDir,
		rotating = rotating, snipshot = self.snipShot)

		return
		
	def baseDataGrabber(self):
		'''Grabs the data from eagle when using an object number/position'''
		self.baseData = eagle.eagle_image_data(self.fileInfo, self.imageParams,
		self.plotParams)
		#we must read the group data first
		try:
			self.baseData.ReadGroupData(centre_fof = self.objectNumber)
			self.particleData = self.baseData.ReadParticleData(
			centre_fof = self.objectNumber)
		except AttributeError:
			#catch the case where we are dealing with a position not an object
			self.baseData.ReadGroupData(centre = self.position)
			self.particleData = self.baseData.ReadParticleData()

		return

	def ensureDir(self, directory):
		'''Checks if a directory exists. If it doesn't, it creates it'''
		if not os.path.isdir(directory):
			print "Trying to create %s" % directory
			os.makedirs(directory)
				
		return

	def makeObjectImage(self, objectNumber = 0, snapNumber = 28,
	imageStyle = ImageStyles.xsmall, angle = 0, snipShot = False):
		"""Make an image of an object. Set snipShot=True to read a
		snipshot rather than a snapshot"""
		self.objectNumber = objectNumber
		self.snapNumber = snapNumber
		self.imageStyle = imageStyle
		self.snipShot = snipShot
		
		self.imageStyleUnpack()
		#package parameters ready for passing to eagle
		self.angle = angle
		self.paramPack()
		self.fileInfoPack(rotating = False)
		
		self.baseDataGrabber()

		self.baseData.plot_image()
		
		return

	def makePosImage(self, position = N.array([0., 0., 0.]), snapNumber = 28,
	imageStyle = ImageStyles.xsmall, angle = 0, snipShot = False):
		"""Make an image of a specified position. Set snipShot=True to read
		a snipshot rather than a snapshot"""
		self.position = position
		self.snapNumber = snapNumber
		self.imageStyle = imageStyle
		self.snipShot = snipShot
		
		self.imageStyleUnpack()
		self.angle = angle
		self.paramPack() 
		self.fileInfoPack(rotating = False)
		
		self.baseDataGrabber()
		
		self.baseData.plot_image()
		 
		return

	def makeStereoObjectImage(self, objectNumber = 0, snapNumber = 28,
	imageStyle = ImageStyles.xsmall, angle = 0, cameraZDistance = False,
	cameraXDistance = 0.1, position = -1, snipShot = False):
		'''This creates a stereo image of a given object, saving in left/right
		subdirectories for individual eyes.
		
		We reccommend that the cameraZDistance/cameraXDistance ~ 100

		Set snipShot = True to read a snipshot rather than snapshot'''
		if position != -1:
			self.position = position
		else:
			self.objectNumber = objectNumber
		#we do the above so we can read the correct place - if we specifiy
		#a position then we read the data from there, else we read obj num
		self.snapNumber = snapNumber
		self.imageStyle = imageStyle
		self.cameraXDistance = cameraXDistance
		self.snipShot = snipShot

		self.imageStyleUnpack()
		self.angle = angle
		if cameraZDistance:
			self.cameraZDistance = cameraZDistance

		self.paramPack()
		self.fileInfoPack(rotating = False)

		self.baseDataGrabber()
		
		# make right
		self.baseData.plot_image(perspective = True,
		camera_x_distance = self.cameraXDistance,
		camera_z_distance = cameraZDistance)
		# make left
		self.baseData.plot_image(perspective = True,
		camera_x_distance = -self.cameraXDistance,
		camera_z_distance = cameraZDistance)

		return
		

if __name__ == "__main__":
	Image = Image()
	Image.makeObjectImage(objectNumber = 1939)

