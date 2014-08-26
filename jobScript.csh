#!/bin/tcsh

# batch script to run a job array making images for movie.
# uses shared memmory machines available on Cosma 5.
# each array job generates one of 400 images.
# The script limits the memory for each job so they can run in parallel.
# 50 Mpc requires 35Gb to run.

# example of how to submit....

#BSUB -P dp004-eagle
#BSUB -q shm5
#BSUB -M 50000  # maximum memory required.  For 25 Mpc
#BSUB -J image_at_position
#BSUB -eo /cosma/home/do004/dc-gues3/LogFiles/ObjectWrapper.e%J-%I
#BSUB -oo /cosma/home/do004/dc-gues3/LogFiles/ObjectWrapper.o%J-%I
#BSUB -m cosma-a

module load python

cd ~/RunDir

python ~/ImageMaker/rgbPlotterMethods.py
