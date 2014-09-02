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

    def __init__(self, rightDir = r'/home/josh/right',
    leftDir = r'/home/josh/left', saveDir = r'/home/josh/3D',
    saveRes = (1920, 1080)):
        self.rightDir = rightDir
        self.leftDir = leftDir
        self.saveDir = saveDir
        self.saveRes = saveRes 

        print "Grabbing filenames from %s" % (rightDir)
        self.fileList = self.fileNameGrabber()

        self.ensureDir(saveDir)

        print "Making 3D images from %s and placing them in %s" % (rightDir,
        saveDir)

        self.makeDir3D()
        
        return

    def ensureDir(self, directory):
        '''Checks if a directory exists. If it doesn't, it creates it'''
        if not os.path.isdir(directory):
            os.makedirs(directory)
                                                    
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

    def imageTo3D(self, pathRight, pathLeft, savePath):
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

        self.aspectRatio = float(outputX)/float(outputY)
        
        # is what we expect y to be smaller than what it is? if so crop in y
        if inputX / self.aspectRatio < inputY:
            diff = inputY - int(inputX / self.aspectRatio)
            if diff % 2 == 0:
                # set top (t) and bottom (b) pixles 'inside' the image
                t = diff / 2
                b = inputY - diff / 2
            else:
                # we have an extra pixel to deal with
                t = diff / 2
                b = (inputY - diff/2) - 1

            l = 0
            r = inputX
        # is what we expect x to be smaller than what it is? if so crop x
        elif inputY * self.aspectRatio < inputX:
            diff = inputX - int(inputY * self.aspectRatio)
            if diff % 2 == 0:
                # set left (l) and right (r) pixels 'inside' the image
                l = diff / 2
                r = inputX - diff / 2
            else:
                # we have an extr pixel to deal with
                l = diff / 2
                r = (inputX - diff/2) - 1

            t = 0
            b = inputY
        # if not caught by the above conditions, then it's already ok AR
        else:
            t = 0
            r = inputX
            l = 0
            b = inputY
        
        cropBox = (l, t, r, b)

        right = right.crop(cropBox)
        left = left.crop(cropBox)
        # now we need to stretch them so they each fill half the canvas

        if outputY % 2 == 0:
            right = right.resize((outputX, outputY/2))
            left = left.resize((outputX, outputY/2))
        else:
            # again, we have an extra pixel to play with
            right = right.resize((outputX, outputY/2 + 1))
            left = left.resize((outputX, outputY/2))

        # we can add the pictures together now
        
        canvas = Image.new("RGBA", self.saveRes)

        # make sure left is top and right bottom or else headache

        canvas.paste(left, (0,0))
        canvas.paste(right, (0, (outputY / 2) + 1))
        
        canvas.save(savePath, "PNG")
        
        return

    def makeDir3D(self):
        '''Iterates over all of the files in the fileList'''
        for file in self.fileList:
            self.imageTo3D(self.rightDir + "/" + file,
            self.leftDir + "/" + file, self.saveDir + "/" + file)

        return

if __name__ == "__main__":
    x = Image3D()
