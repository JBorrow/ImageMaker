'''

These files are meant to replace make_standard_images.py as it is an
uncommented, unmodular mess (sorry Richard...)

This file is a class containing dictionaries for holding the styles for the
images.

Josh Borrow
Durham University
Institute for Computational Cosmology
07/07/2014
'''

import numpy as N

class ImageStyles:
    '''
    This class holds the image styles for creating the images.
    '''

    xxsmall = {
    'name' : 'xxsmall',
    'width' : 0.1,
    'scale' : [3.0, 10000.],
    'star_scale_factor' : 5.,
    'dark_scale_factor' : 100000.,
    'gas_cmap' : None,
    'T_limits' : [3.8,4.0,4.5],
    'pixels' : [512,512]
    }

    xxsmall_2 = {
    'name' : 'xxsmall_2',
    'width' : 0.1,
    'scale' : [30.0, 10000.],
    'star_scale_factor' : 5.,
    'dark_scale_factor' : 100000.,
    'gas_cmap' : None,
    'T_limits' : [3.8,4.0,4.5],
    'pixels' : [512,512]
    }

    xxsmall_gist = {
    'name' : 'xxsmall_gist',
    'width' : 0.1,
    'scale' : [30.0, 10000.],
    'star_scale_factor' : 5.,
    'dark_scale_factor' : 100000.,
    'gas_cmap' : 'gist_earth',
    'T_limits' : [3.8,4.0,4.5],
    'pixels' : [512,512]
    }

# linear scaled version of the one above. Good for gas, but not for stars
    xxsmall_linear = {
    'name' : 'xxsmall_linear',
    'width' : 0.1,
    'scale' : [0.1, 1000.],
    'star_scale_factor' : 5.,
    'dark_scale_factor' : 100000.,
    'gas_cmap' : None,
    'T_limits' : [3.8,4.0,4.5],
    'pixels' : [512,512],
    'use_logh' : False
    }

    xsmall = {
    'name' : 'xsmall',
    'width' : 0.5,
    'scale' : [5.0, 10000.],
    'star_scale_factor' : 3.,
    'dark_scale_factor' : 100000.,
    'gas_cmap' : None,
    'T_limits' : [3.8,4.0,4.5],
    'pixels' : [512,512]
    }

    small = {
    'name' : 'small',
    'width' : 1.0,
    'scale' : [5.0, 10000.],
    'star_scale_factor' : 3.,
    'dark_scale_factor' : 100000.,
    'gas_cmap' : None,
    'T_limits' : [3.8,4.0,4.5],
    'pixels' : [512,512]
    }

    medium_hi = {
    'name' : 'medium_hi',
    'width' : 2.0,
    'scale' : [5.0, 10000.],
    'star_scale_factor' : 3.,
    'dark_scale_factor' : 100000.,
    'gas_cmap' : None,
    'T_limits' : [3.8,4.0,4.5],
    }

    medium = {
    'name' : 'medium',
    'width' : 2.0,
    'scale' : [2.0, 1000.],
    'star_scale_factor' : 2.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.]
    }

    joshrot = {
    'name' : 'joshrot',
    'width' : 2.0,
    'scale' : [2.0, 1000.],
    'star_scale_factor' : 2.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    "pixels" : [1920,1920]
    }

    large = {
    'name' : 'large',
    'width' : 5.0,
    'scale' : [1.0, 1000.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.]
    }

    xlarge = {
    'name' : 'xlarge',
    'width' : 10.0,
    'scale' : [1.0, 1000.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    }

    xlarge_hr = {
    'name' : 'xlarge_hr',
    'width' : 10.0,
    'scale' : [1.0, 1000.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'pixels' : [1920,1920]
    }

    xxlarge = {
    'name' : 'xxlarge',
    'width' : N.array([20., 20., 10.]),
    'scale' : [1.0, 1000.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'pixels' : [2048,2048]
    }

    exhibition = {
    'name' : 'exhibition',
    'width' : N.array([50., 50., 10.]),
    'scale' : [1.0, 500.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' :  100000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'pixels' : [2048,2048]
    }

    exhibition2 = {
    'name' : 'exhibition2',
    'width' : N.array([47., 30., 20.]),
    'scale' : [1.0, 500.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' :  100000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'pixels' : [2048*47./50.,2048*30./50.],# 4096 is too big to create cube
    'opacity' : 0.1,
    'text' : False
    }

    exhibition_rotation = {
    'name' : 'exhibition_rotation',
    'width' : 45,
    'scale' : [1.0, 500.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' :  100000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'pixels' : [512,512],# 4096 is too big to create cube
    'opacity' : 0.2,
    'text' : False
    }

    supersize = {
    'name' : 'supersize',
    'width' : N.array([100., 100., 20.]),
    'scale' : [0.2, 500.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'pixels' : [2048,2048],
    'opacity' : 0.2,
    'text' : False
    }

    supersize_rotation = {
    'name' : 'supersize_rotation',
    'width' : 100.,
    'scale' : [0.2, 500.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'pixels' : [1024,1024],
    'opacity' : 0.2,
    'text' : False
    }

    supersize_simple = {
    'name' : 'supersize_simple',
    'width' : N.array([100., 100., 20.]),
    'scale' : [0.2, 500.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'pixels' : [2048,2048]
    }

    whole25 = {
    'name' : 'whole25',
    'width' : N.array([25., 25., 25.]),
    'scale' : [0.2, 500.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'pixels' : [2048,2048],
    'opacity' : 0.2,
    'text' : False
    }

	
    supersize80 = {
    'name' : 'supersize80',
    'width' : N.array([80., 80., 80.]),
    'scale' : [0.2, 500.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'pixels' : [4096,4096],
    'opacity' : 0.2,
    'text' : False
    }

    wanhundrad = {
    'name' : 'wanhundrad',
    'width' : N.array([100., 100., 100.]),
    'scale' : [0.2, 500.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'pixels' : [4096,4096],
    'opacity' : 0.2,
    'text' : False
    }

    supersize_super_hr = {
    'name' : 'supersize_super_hr',
    'width' : N.array([100., 100., 20.]),
    'scale' : [0.2, 500.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'pixels' : [12288,12288],
    'text' : False,
    }

    josh_3D = {
    'name' : "josh_3D",
    'width' : N.array([10.,10.,10.]),
    'scale' : [0.2, 500.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'pixels' : [2400,2400],
    'text' : False,
    }

    custom = {
    'name' : 'custom',
    'width' : 15.0,
    'scale' : [1.0, 1000.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.]
    }

    xlarge_rotation = {
    'name' : 'xlarge_rotation',
    'width' : 10.0,
    'scale' : [1.0, 1000.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'opacity' : 0.2,
    'text' : False,
    'camera_z_distance' : 20
    }

    medium_rotation = {
    'name' : 'medium_rotation',
    'width' : 2.0,
    'scale' : [2.0, 1000.],
    'star_scale_factor' : 2.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'opacity' : 0.2,
    'text' : False,
    'camera_z_distance' : 4.
    }

    app = {
    'name' : 'app',
    'width' : 50.0,
    'scale' : [0.3, 1000.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'camera_z_distance' : 0.0,
    'pixels' : [4048,4048]
    }

    long_shot = {
    'name' : 'long_shot',
    'width' : [10.0,10.0,20.0],
    'scale' : [0.3, 1000.],
    'star_scale_factor' : 1.,
    'dark_scale_factor' : 50000.,
    'gas_cmap' : None,
    'T_limits' : [4.5,5.5,10.],
    'camera_z_distance' : 0.0,
    'pixels' : [512,512]
    }


    def __init__(self):
        return



if __name__ == "__main__":
    print "This test code prints out the xsmall type"
    print ImageStyles.xsmall
