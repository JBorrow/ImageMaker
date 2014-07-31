'''
This script will grab the first frame of a movie, and export it as a .png
with the filename of the 'type' of movie.

Josh Borrow
31/07/2014
Institute For Computational Cosmology
'''

import sys
import subprocess

args = sys.argv

#put the types of movie here
types = ['gas','dark','star','bh','phase','hi']

movieaddon = "_movie.avi"

if "-path" in args:
    path = args[args.index("-path")]
else:
    path = "."

for type in types:
    moviename = path + type + movieaddon
    command = "ffmpeg -i %s -r 1 -s 200x200 -f image2 %s.png" % (moviename, path + type)

    subprocess.call(command.split())
