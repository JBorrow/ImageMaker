ImageMaker
==========

The ImageMaker module creates some prompts to enter the stuff for creating images from the Eagle project.

Original base code (make\_standard\_images.py) by Richard Bower, however
this module was written by Joshua Borrow.

Using the program
-----------------

The program is very simple to use - it simply asks you some questions about what
you want to make from your images and then makes them using the Eagle routines.

Here is an example:
```
What type of image would you like?: position
Which snapshots do you want to use? Enter 'finished' once you are done: 28
Which snapshots do you want to use? Enter 'finished' once you are done: 27
Which snapshots do you want to use? Enter 'finished' once you are done: 26
Which snapshots do you want to use? Enter 'finished' once you are done: finished
What sizes do you require? Enter 'finished' once you are done: xsmall
What sizes do you require? Enter 'finished' once you are done: large
What sizes do you require? Enter 'finished' once you are done: finished
Please enter your co-ordniates in units of Mpc
Please enter the first co-ordinate: 28
Please enter the second co-ordinate: 39
Please enter the third co-ordinate: 10
Do you want a rotating image? (y/n): y
Do you want descriptive text on the image? (y/n): y
Here is a list of the variables that are relevant:
type:  position
snap_list:  [28, 27, 26]
size_list:  ['xsmall', 'large']
type:  position
position:  [ 28.  39.  10.]
rotating:  True
text:  True
Are you happy with these?
Type 'yes' to make the images and start the process or no to quit:
```

Functions
---------

###askForUserType()

Asks the user for their type and raises an exception if somehow
broken. Also accepts 'exit' which quits the program with exit code 1.

###askForImageSize()

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

###askForType()

Asks for the type of image that the user wants to create. Possible
types:
```
    position - makes an image at some given co-ords
    objectimage - makes an image based on object numbers
    objectgallery - makes a "gallery" of many object numbers
    specialgallery - makes a supersize image with lots of xsmall
	images on top
```

###askForPosition()

Asks for the position if the position is chosen as the type. Asks for
the co-ordinates and then puts them into a numpy array.

Enter in units of Mpc

###trueFalse(askerstring)

Asks for a yes or no input. Askerstring is printed on the same line
as the input. Inputs can be in the form:

```
	yes = ["yes","YES","y","Y"]
	no = ["no","n","N","NO"]
```

Outputs True/False for yes/no respectively.


###singleVarAsker(askerstring,default)

A very simple variable asker - prints askerstring and waits for input.
Outputs an integer. Used for asking for number of friends of friends etc.

###miniTypeAsker()

Asks for the type of the miniature images for the 'special gallery'.

Acceptable types:

```
	'gas'
	'dark'
	'hi'
	'phase'
	'star'
```

###areYouSure(valuedictionary, items)

This goes through the variables and checks if you are happy. If you are not
it will quit - exit code 3.
