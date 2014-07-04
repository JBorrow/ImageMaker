ImageMaker
==========

The ImageMaker module creates some prompts to enter the stuff for creating images from the Eagle project.

Original base code (make_standard_images.py) by Richard Bower, however
this module was written by Joshua Borrow.

Functions
--------

###askForUserType()

Asks the user for their type and raises an exception if somehow
broken. Also accepts 'exit' which quits the program with exit code 1.

###askForImageType()

Asks the user for the type of image required. The currently accepted
types are:
```
		xxsmall 				xxlarge 			        app
		xxsmall-2 				exhibition  				long_shot
		xxsmall-gist 			exhibition2
		xxsmall-linear 	   	    exhibition_rotation
		xsmall 					supersize
		small					supersize_rotation
		medium-hi 				supsersize_simple
		medium 					custom
		large 					xlarge_rotation
		xlarge 				   	medium_rotation
```

###askForObjectNumbers()

Similar to above. This function asks for the object lists and checks
to see if they are integers in the range 0-9999.

###askForSnaps()

Again, very similar to above, but only accepts in range 0-28.
