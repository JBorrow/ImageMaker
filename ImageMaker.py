'''
Acts as a wrapper for Richard Bower's script that is called
'make_standard_images.py'. This wrapper makes the script much
easier to use as previously the actual file was needed to be
each and every use.

Important: running this script will create directories within
your current one if neccessary, and the data will be stored
as:

/Webpage/<Object Number, Centre co-ords, Gallery>/Snapshot
<snapshotnumber>/<size>

Josh Borrow
04/07/2014
'''

import numpy as N
#import make_standard_images as msi

#initialise variables - we hold in a dictionary as this is easiest.
variables = {
'snap_list' : [], #list of snapshots that are required
'object_list' : [], #list of objects that are required
'size_list' : ['xsmall'], #sizes chosen from the styles DB
'position' : N.array([0,0,0]), #position center
'type' : 'position', #types of images, see documentation
'text' : True, #text e.g. position on image
'deletefiles' : True, #cleans up after making gallery
'nfof' : 50, #number of fof
'centre_fof' : 0,
'first_fof' : 0,
'fof_step' : 1,
'subsample' : 1, #subsample factor to not read in all particles
'gas_cmap' : None,

#just for rotations

'rotating' : False, #rotating image only works with normal/position


#just for 'special' gallery - EXPERIMENTAL AND DOESN'T WORK YET

'remake_gallery' : True, #remake gallery of xsmall images
'minitype' : 'gas', #type of the miniature images
'label_only' : False, #no minature images if True
}

#questioning variables

usertype = ""


#questioning functions

def askForUserType():
	'''
	Asks the user for their type and raises an exception if somehow broken. Also
	accepts 'exit' which quits the program with exit code 1.
	'''
	usertype = ""

	while usertype not in ["b","a","exit"]:
		usertype = raw_input("Would you like a basic options list or an advanced options list? (b/a): ")

	if usertype == "b":
		return "b"
	elif usertype == "a":
		return "a"
	elif usertype == "exit":
		print "Exiting..."
		exit(1)
	else:
		raise InputError(msg = "I don't know how, but you broke me in the askForUserType() function")

def askForImageSize():
	'''
	Asks the user for the type of image required. The currently accepted types are:
		xxsmall 				xxlarge 					app
		xxsmall-2 				exhibition  				long_shot
		xxsmall-gist 			exhibition2
		xxsmall-linear 			exhibition_rotation
		xsmall 					supersize
		small					supersize_rotation
		medium-hi 				supsersize_simple
		medium 					custom
		large 					xlarge_rotation
		xlarge 					medium_rotation

	'''

	possiblesizes = ["xxsmall" 			,	"xxlarge", 				"app",
					 "xxsmall-2" 		,	"exhibition"  			"long_shot",
					 "xxsmall-gist" 	,	"exhibition2",
					 "xxsmall-linear" 	,	"exhibition_rotation",
					 "xsmall"			,	"supersize",
					 "small"			,	"supersize_rotation",
					 "medium-hi" 		,	"supsersize_simple",
					 "medium" 			,	"custom",
					 "large" 			,	"xlarge_rotation",
					 "xlarge" 			,	"medium_rotation"]

	isokay = False #this is set to false initially, as we are going to perform checks based on it

	while not isokay:
		size_list = [] #for appending later
		input = ""
		correctlist = True

		while input != "finished":
			input = str(raw_input("What sizes do you require? Enter 'finished' once you are done: "))
			if input != "finished" and input != "":
				size_list.append(input)

		for size in size_list:
			if size not in possiblesizes:
				print '''Please try again. If you don't know the possible sizes, please consult
the documentation. First bad size: ''', size
				correctlist = False
				break
			else:
				None

		if correctlist == False:
			continue
		else:
			isokay = True

	return size_list

def askForObjectNumbers():
    '''
    This function asks for the object lists and checks to see if they are
    integers in the range 0-9999.
    '''

    possibleobjects = list(range(10000)) #number of possible objects max = 9999, min = 0

    isokay = False #this is set to false initially, as we are going to perform checks based on it

    while not isokay:
		object_list = [] #for appending later
		input = ""
		correctlist = True

		while input != "finished":
			input = raw_input("Which objects do you want to image? Enter 'finished' once you are done: ")
			if input != "finished" and input != "":
				object_list.append(int(input))

		for number in object_list:
			if number not in possibleobjects:
				print '''Please try again. Objects must be integers in range 0-9999. First bad: ''', number
				correctlist = False
				break
			else:
				None

		if correctlist == False:
			continue
		else:
			isokay = True

    return object_list


def askForSnaps():
    '''
    This function asks for the snapshot you want and checks it's in the range 0-28
    '''

    possibleobjects = list(range(29)) #number of possible objects max = 29, min = 0

    isokay = False #this is set to false initially, as we are going to perform checks based on it

    while not isokay:
		snap_list = [] #for appending later
		input = ""
		correctlist = True

		while input != "finished":
			input = raw_input("Which snapshots do you want to use? Enter 'finished' once you are done: ")
			if input != "finished" and input != "":
				snap_list.append(int(input))

		for snap in snap_list:
			if snap not in possibleobjects:
				print '''Please try again. Objects must be integers in range 0-9999. First bad: ''', snap
				correctlist = False
				break
			else:
				None

		if correctlist == False:
			continue
		else:
			isokay = True

    return snap_list

def askForType():
    '''
    Asks for the type of images that you want to create. Possible types include:
    "position" - makes an image at some given co-ords
    "objectimage" - makes an image based on object numbers
    "objectgallery" - makes a "gallery" of many object numbers
    "specialgallery" - makes a supersize image with lots of xsmall images on top
    '''

    possibletypes =["position",
                      "objectimage",
                      "objectgallery",
                      "specialgallery"]

    while True:
        input = str(raw_input("What type of image would you like?: "))

        if input in possibletypes:
            return input

def askForPosition():
    '''
    Asks for the position if the position is chosen as the type. Asks for
    the co-ordinates and then puts them into a numpy array.
    Enter in units of Mpc
    '''

    print 'Please enter your co-ordniates in units of Mpc'
    x = float(raw_input("Please enter the first co-ordinate: "))
    y = float(raw_input("Please enter the second co-ordinate: "))
    z = float(raw_input("Please enter the third co-ordinate: "))

    return N.array([x,y,z])

def trueFalse(askerstring):
	'''
	Input  yes/no or other ways of saying so and returns True/False as
	appropriate.
	'''
	yes = ["yes","YES","y","Y"]
	no = ["no","n","N","NO"]

	input = ""

	while input not in (yes+no):
		input = str(raw_input(askerstring))

	if input in yes:
		return True
	elif input in no:
		return False
	else:
		raise InputError(msg = "How did you do that? In trueFalse function if statement")


def singleVarAsker(askerstring,default):
	'''
	A simple variable query - with no extreme values. Output type = int
	'''
	input = ""

	while input == "":	#these statements are used incase return key pressed
		input = str(raw_input(askerstring + " Default = " + str(default) + ": "))

	outs = int(input)

	return outs

def miniTypeAsker():
	'''
	Asks for the type of the miniature images for the 'special gallery'.

	Acceptable types:
	'gas'
	'dark'
	'hi'
	'phase'
	'star'
	'''

	possibletypes = ['gas',
					 'dark',
					 'hi',
					 'phase',
					 'star']

	input = ""

	while input not in possibletypes:
		input = str(raw_input("What type of miniature image would you like superimposed: "))

	return input

def areYouSure(valuedictionary, items):
	'''
	This goes through the variables and checks if you are happy. If you are not
	it will quit - exit code 3.
	'''

	print "Here is a list of the variables that are relevant:"

	for item in items:
		print item + ": " , valuedictionary[item]

	print "Are you happy with these?"

	makeornot = trueFalse("Type 'yes' to make the images and start the process or no to quit: ")

	if makeornot == True:
		return
	else:
		print 'Exiting...'
		exit(3)


#begin questioning

variables['type'] = askForType()

variables['snap_list'] = askForSnaps()

variables['size_list'] = askForImageSize()

if variables['type'] == 'position':

	variables['position'] = askForPosition()

	variables['rotating'] = trueFalse("Do you want a rotating image? (y/n): ")

	if 'supersize' in variables['size_list'] and variables['rotating'] == True:
		print 'WARNING: MAKING ROTATING IMAGES USES LOTS OF MEMORY, ESPECIALLY WITH SUPSERSIZE'
		keepgoing = trueFalse("Continue - you might break Cosma...? (y/n): ")
		if keepgoing == False:
			print 'Exiting before you do any damage...'
			exit(-1)

	variables['text'] = trueFalse("Do you want descriptive text on the image? (y/n): ")

	areYouSure(variables,['type','snap_list','size_list','type','position','rotating','text'])

	# STATEMENT FOR MAKING IMAGE HERE FOR TYPE = POSITION

elif variables['type'] in ["objectimage","objectgallery","specialgallery"]:

	variables['object_list'] = askForObjectNumbers()

	if variables['type'] == 'objectimage':

		variables['rotating'] = trueFalse("Do you want a rotating image? (y/n): ")

		areYouSure(variables,['type','snap_list','size_list','type','object_list','rotating'])

		# STATEMENT FOR MAKING IMAGE HERE FOR TYPE = OBJECTIMAGE

	elif variables['type'] in ["objectgallery","specialgallery"]:

		if askForUserType() == "b":

			areYouSure(variables,['type','snap_list','size_list','type','position','rotating','text'])

			if variables['type'] == 'objectgallery':
				print "object"
				# STATEMENT FOR MAKING IMAGE HERE FOR TYPE = OBJECTGALLERY

			elif variables['type'] == 'specialgallery':
				print "special"
				# STATEMENT FOR MAKING IMAGE HERE FOR TYPE = SPECIALGALLERY

			else:
				print "Invalid inputs"

		else:
			print "advanced"
			#PUT ADVANCED OPTIONS HERE



	else:
		print "Invalid inputs"
else:
	print "Invalid inputs"
	exit(-1)
