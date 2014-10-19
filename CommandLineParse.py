"""This file contains a class that parses the command line arguments for making
images for The EAGLE Project. This is separate so it may be used in more than
one script, cutting down on code re-use.

Command-line arguments it looks for:
	-r <t/f>                            Rotating?
	-o <objectNumber>                   Object number
	-c "<x> <y> <z>"                    Center. If specified ignores Obj num
	-sn <snapNumber>                    Snapshot number
	-sd <saveDir>                       Save directory. No ~/, only direct
										NO DEFAULT - REQUIRED
	-is <imageStyle>                    Image style name (see ImageStyles.py)
	-pp "<t/f> <t/f> <t/f> <t/f> <t/f>" Partplot, default "t t t t t"
	-t <t/f>                            Text?
	-nf <nFrames>                       Number of frames for rotation
	-nc <nCores>                        Number of cores to use at once for rot
	-3D <t/f>                           3D? Below only make sense if true
	-cxd <cameraXDistance>              Distance from center to camera
	-czd <cameraZDistance>              Distance from eye to nose for 3D
										We recommend 1:75 cxd:czd

				#############################################
				# Josh Borrow                               #
				# Institute For Computational Cosmology     #
				# Durham University                         #
				# The EAGLE Project                         #
				# joshua.borrow@durham.ac.uk                #
				# 24/08/2014                                #
				#############################################
"""
from ImageStyles import *
import numpy as N


class CommandLineArguments(object):
	"""This class contains all of the functions to parse the data, storing them
	in itself. E.g. the partplot list will be parsed and set as self.partplot
	"""
	def __init__(self, commandLineArguments):
		self.CLI = commandLineArguments

		if "-r" in self.CLI:
			self.rotating = self.argumentGrabber("-r")
		else:
			self.rotating = False

		if "-o" in self.CLI:
			self.objectNumber = int(self.argumentGrabber("-o"))
		else:
			print "Warning: no object number specified. If you used center, ignore"
			self.objectNumber = 0

		if "-c" in self.CLI:
			rawPosition = self.argumentGrabber("-c")
			self.position = self.centreConvert(rawPosition)
		else:
			self.position = -1

		if "-sn" in self.CLI:
			self.snapNumber = int(self.argumentGrabber("-sn"))
		else:
			print "Warning: no snap specified - default = 28"
			# 28 == z=0
			self.snapNumber = 28

		if "-sd" in self.CLI:
			self.saveDir = self.argumentGrabber("-sd")
		else:
			print "ERROR: No save directory specified"
			print "FILE: CommandLineParse.py in ImageMaker"
			exit(-1)

		if "-is" in self.CLI:
			rawImageStyle = self.argumentGrabber("-is")
			self.imageStyle = self.imageStyleConvert(rawImageStyle)
		else:
			print "Warning: no image style specified - default = xsmall"
			self.imageStyle = ImageStyles.xsmall

		if "pp" in self.CLI:
			rawPartplot = self.argumentGrabber("pp")
			self.partplot = self.partplotConvert(rawPartplot)
		else:
			self.partplot = [True, True, True, True, True]

		if "-t" in self.CLI:
			self.text = self.trueFalse(self.argumentGrabber("-t"))
		else:
			print "Warning: text will be on the image"
			self.text = True

		if "-nf" in self.CLI:
			self.nFrames = int(self.argumentGrabber("-nf"))
		else:
			self.nFrames = 360

		if "-nc" in self.CLI:
			self.nCores = int(self.argumentGrabber("-nc"))
		else:
			# Reccommended number of cores for cosma-a/b/c/e/f - Lydia
			self.nCores = 12

		if "-3D" in self.CLI:
			self.ThreeD = self.trueFalse(self.argumentGrabber("-3D"))
		else:
			self.ThreeD = False

		if "-cxd" in self.CLI:
			self.cameraXDistance = float(self.argumentGrabber("-cxd"))
		else:
			if self.ThreeD:
				self.cameraXDistance = 0.75
			else:
				self.cameraXDistance = 0

		if "-czd" in self.CLI:
			self.cameraZDistance = float(self.argumentGrabber("-czd"))
		elif 'camera_z_distance' in self.imageStyle.keys():
			self.cameraZDistance = self.imageStyle['camera_z_distance']
			self.perspective = True
		else:
			# let the code decide
			self.cameraZDistance = None
			self.perspective = False

		return

	def argumentGrabber(self, identifier):
		"""Grabs the command line argument given an identifier, e.g. "-o\""""
		return self.CLI[self.CLI.index(identifier) + 1]

	def trueFalse(self, arg):
		"""Supply with either 't' or 'f' and converts to True/False"""
		if arg == 't':
			return True
		elif arg == 'f':
			return False
		else:
			print "You supplied me with %s instead of t or f" % arg
			raise UserWarning

	def centreConvert(self, arg):
		"""Takes a string and puts it in a numpy array, e.g.:
		"0.12 123.4 0.21" -> numpy.array([0.12, 123.4, 0.21])"""
		split = arg.split()
		centreList = []
		for value in split:
			centreList.append(float(value))

		return N.array(centreList)

	def imageStyleConvert(self, arg):
		"""Takes the string and compares it with a list of possible names in the
		ImageStyle class, then returns the dictionary associated with it"""
		if 'xxsmall' == arg:
			imageStyle = ImageStyles.xxsmall
		elif 'xxsmall_2' == arg:
			imageStyle = ImageStyles.xxsmall_2
		elif 'xxsmall_gist' == arg:
			imageStyle = ImageStyles.xxsmall_gist
		elif 'xxsmall_linear' == arg:
			imageStyle = ImageStyles.xxsmall_linear
		elif 'xsmall' == arg:
			imageStyle = ImageStyles.xsmall
		elif 'small' == arg:
			imageStyle = ImageStyles.small
		elif 'medium_hi' == arg:
			imageStyle = ImageStyles.medium_hi
		elif 'medium' == arg:
			imageStyle = ImageStyles.medium
		elif 'medium_rotation' == arg:
			imageStyle = ImageStyles.medium_rotation
		elif 'large' == arg:
			imageStyle = ImageStyles.large
		elif 'xlarge' == arg:
			imageStyle = ImageStyles.xlarge
		elif 'xlarge_rotation' == arg:
			imageStyle = ImageStyles.xlarge_rotation
		elif 'xxlarge' == arg:
			imageStyle = ImageStyles.xxlarge
		elif 'exhibition' == arg:
			imageStyle = ImageStyles.exhibition
		elif 'exhibition2' == arg:
			imageStyle = ImageStyles.exhibition2
		elif 'exhibition_rotation' == arg:
			imageStyle = ImageStyles.exhibition_rotation
		elif 'supersize' == arg:
			imageStyle = ImageStyles.supersize
		elif 'supersize_rotation' == arg:
			imageStyle = ImageStyles.supersize_rotation
		elif 'supersize_simple' == arg:
			imageStyle = ImageStyles.supersize_simple
		elif 'custom' == arg:
			imageStyle = ImageStyles.custom
		elif 'app' == arg:
			imageStyle = ImageStyles.app
		elif 'long_shot' == arg:
			imageStyle = ImageStyles.long_shot
		else:
			print "ERROR: Could not find your image style."
			print "FUNCTION: imageStyleConvert()"
			print "FILE: CommandLineParse.py"
			exit(-1)
			
		return imageStyle

	def partplotConvert(self, arg):
		"""Converts a string of t/f to True/False list"""
		rawPartplot = arg.split()
		partplot = []
		for boolean in rawPartplot:
			partplot.append(self.trueFalse(boolean))

		return partplot

if __name__ == "__main__":
	"""Scripts the process using the above class"""
	import sys
	from RotationClass import *

	args = sys.argv
	# Extract the arguments
	CLI = CommandLineArguments(args)
	# Rotation is a superclass - has all single image stuff inside
	ImageMaker = Rotation(partplot=CLI.partplot, saveDir=CLI.saveDir)

	if CLI.rotating:
		ImageMaker.makeObjectRotation(imageStyle=CLI.imageStyle,
									  snapNumber=CLI.snapNumber,
									  objectNumber=CLI.objectNumber,
									  text=CLI.text,
									  nFrames=CLI.nFrames,
									  nCores=CLI.nCores,
									  cameraXDistance=CLI.cameraXDistance,
									  cameraZDistance=CLI.cameraZDistance,
									  position=CLI.position)
	else:
		if CLI.position is not -1:
			ImageMaker.makePosImage(position=CLI.position,
									snapNumber=CLI.snapNumber,
									imageStyle=CLI.imageStyle)

		elif not CLI.ThreeD:
			ImageMaker.makeObjectImage(objectNumber=CLI.objectNumber,
									   snapNumber=CLI.snapNumber,
									   imageStyle=CLI.imageStyle)
		else:
			# This deals with position + objectNumber internally
			ImageMaker.makeStereoObjectImage(objectNumber=CLI.objectNumber,
											 snapNumber=CLI.snapNumber,
											 imageStyle=CLI.imageStyle,
											 angle=0,
											 cameraZDistance=CLI.cameraZDistance,
											 cameraXDistance=CLI.cameraXDistance,
											 position=CLI.position)