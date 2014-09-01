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
    saveDir = '~/3D'):
        self.rightDir = rightDir
        self.leftDir = leftDir
        self.saveDir = saveDir
            
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

        if not cleanListRight == cleanListLeft:
            print "ERROR: Filenames in left/right directories are not the same."
            exit(-1)

        return cleanListRight

    def imageTo3D(self, fileName):
        return
