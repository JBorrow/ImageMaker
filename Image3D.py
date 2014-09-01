'''This makes the image 3-D by combining left and right 'eyes'.

Requires that both of the 'eyes' have the same filename, but in different
directories. It automatically scrapes these directories and stitches them
together, and places the 

Joshua Borrow
01/09/2014
Institute For Computataional Cosmology, Durham University
The EAGLE Project
joshua.borrow@durham.ac.uk
'''

from PIL import Image
import os

class Image3D(object):
    '''Contains all of the methods used to change the data into 3-D formats'''

    def __init__(self, rightDir = '~/right', leftDir = '~/left',
    saveDir = '~/3D', saveRes = (1920, 1080)):
        self.rightDir = rightDir
        self.leftDir = leftDir
        self.saveDir = saveDir
        self.saveres = saveRes 

        print "Grabbing filenames from %s" % (rightDir)
        self.fileNameGrabber()

        return

    def fileListClean(self, list):
        '''Looks in list, and checks if the values are hidden, if they are they
        get removed''' 
        cleanList = []
        
        for value in list:
            if value[0] == ".":
                continue
            else:
                cleanList.append(value)

        return cleanList

    def fileNameGrabber(self):
        initialListRight = os.listdir(self.rightDir)
        initialListLeft = os.listdir(self.leftDir)
         
        cleanListRight = self.fileListClean(initialListRight)
        cleanListLeft = self.fileListClean(initialListLeft)

        if cleanListRight != cleanListLeft:
            print "ERROR: Filenames in left/right directories are not the same."
            print "FILE: Image3D.py" 
            exit(-1)

        return cleanListRight

    def imageTo3D(self, pathRight, pathLeft):
        '''Takes two paths and combines them to make a 3D image of the same
        name'''
        right = Image.open(pathRight)
        left = Image.open(pathLeft)
        
        if right.size != left.size:
            print "ERROR: Images are not the same size"
            print "FILE: Image3D.py" 
            exit(-1)

        # now we figure out the geometry of the situation
        inputX = right.size[0]
        inputY = right.size[1]
        outputX = self.saveRes[0]
        outputY = self.saveRes[1]

        # if images are bigger, crop
        if inputX > outputX:
            diffX = inputX - outputX
            if diffX % 2 == 0:
                leftCrop = diffX/2
                rightCrop = inputX - diffX/2
            else:
                # give right the extra pixel
                leftCrop = diffX/2
                rightCrop = (inputX - (diffX/2)) - 1
            
        else:
            rightCrop = inputX
            leftCrop = 0

        if inputY > outputY
            diffY = inputY - outputY
            if diffY % 2 == 0:
                topCrop = diffY/2
                bottomCrop = inputY - diffY/2
            else:
                # give bottom the extra pixel
                topCrop = diffY/2
                bottomCrop = (inputY - (diffY/2)) - 1
                
        else:
            topCrop = 0
            bottomCrop = inputY 

        return
