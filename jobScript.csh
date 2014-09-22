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
#BSUB -eo /cosma/home//mphf18/LogFiles/ObjectWrapper.e%J-%I
#BSUB -oo /cosma/home//mphf18/LogFiles/ObjectWrapper.o%J-%I
#BSUB -m cosma-a

module load python
cd /cosma5/data/Eagle/rgbTestRuns/Planck/L0025N0376/PE/Z0p10_W1p00_E_3p0_0p3_ALPHA1p0e6_rhogas1_reposlim3p0soft_100mgas/
python ~/ImageMaker/RotationClass.py
