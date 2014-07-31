'''
This script will grab the first frame of a movie, and export it as a .png
with the filename of the 'type' of movie.

Josh Borrow
31/07/2014
Institute For Computational Cosmology
'''

import sys
import subprocess
import time
import os

args = sys.argv

#put the types of movie here
types = ['gas','dark','star','bh','phase','hi']

movieaddon = "_movie.avi"

if "-path" in args:
    path = args[args.index("-path")]
else:
    path = "./"

for type in types:
	moviename = path + type + movieaddon
	command = "ffmpeg -i %s -t 1 -ss 26 -s 200x200 -f image2 %s_temp.png" % (moviename, path + type)

	subprocess.call(command.split())
	time.sleep(2)
	converter = ['convert', '%s_temp.png' % (type),'-font','Helvetica','-pointsize','40','-gravity','center',
				 '-draw','fill white text 0,0 %s' % (type.upper()),'%s.png' % (type)]

	print converter
	subprocess.call(converter)
	time.sleep(2)

#cleanup
os.system('rm ' + path + '*temp.png')
