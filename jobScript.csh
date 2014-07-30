#!/bin/tcsh

# batch script to run a job array making images for movie.
# uses shared memmory machines available on Cosma 5.
# each array job generates one of 400 images.
# The script limits the memory for each job so they can run in parallel.
# 50 Mpc requires 35Gb to run.

# example of how to submit....

#BSUB -P dp004-eagle
#BSUB -q shm5
#BSUB -M 150000  # maximum memory required.  For 25 Mpc
#BSUB -J image_at_position
#BSUB -eo ~/LogFiles/ObjectWrapper.e%J-%I
#BSUB -oo ~/LogFiles/ObjectWrapper.o%J-%I
#BSUB -m cosma-f

module load python

python ~/ImageMaker/ObjectWrapper.py -r t -sl "xlarge_hr" -p "t t t t t" -ol "7"