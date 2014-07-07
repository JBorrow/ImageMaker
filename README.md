ImageMaker
==========

The ImageMaker project is used to create images for the Eagle Project.

These files hold the code that uses some of the Eagle plotting routines.

### ImageMaker.py ###

This file creates some prompts to help in the creation of images.

It is intended for basic use, as it is *realtively* user friendly.

I don't know if it breaks anything yet.

It is also unfinished.

Last updated: 07/07/2014

### ImageStyles.py ###

After realising a dictionary of dictionaries isn't great for holding the
styles used to create the images, I created a class that holds them
under variable names. This is much easier to work with and means that they
can be in a separate file to the actual functions.

This means that there is much less of a chance of breaking things.

Last updated: 07/07/2014


### rgbPlotterMethods.py

This is the actual plotting methods. It has been adapted from the code in:

	make_standard_images.py

Hopefully this will work a lot better and will be a lot easier to work with.

It will also allow us to create command-line input in a separate file as
*all* variables will be able to be inputed rather than using local variables.

Last updated : 07/07/2014
