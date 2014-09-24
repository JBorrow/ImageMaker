'''This file contains a class that parses the command line arguments for making
images for The EAGLE Project. This is separate so it may be used in more than
one script, cutting down on code re-use.

Command-line arguments it looks for:
    -r <t/f>                            Rotating?
    -o <objectNumber>                   Object number
    -c "<x> <y> <z>"                    Center. If specified ignores Obj num
    -sn <snapNumber>                    Snapshot number
    -sd <saveDir>                       Save directory. No ~/, only direct
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
'''

class CommandLineArguments(object):
    '''This class contains all of the functions to parse the data, storing them
    in itself. E.g. the partplot list will be parsed and set as self.partplot
    '''
    def __init__(self, commandLineArguments):
        self.CLI = commandLineArguments
        
        return
        
     
