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

#initialise variables

snap_list = [] #list of snapshots that are required
object_list = [] #list of objects that are required
size_list = ['xsmall'] #sizes chosen from the styles DB
position = N.array([0,0,0]) #position center
types = ['normal'] #types of images, see documentation
text = True #text e.g. position on image 
deletefiles = True #cleans up after making gallery
nfof = 50 #number of fof
centre_fof = 0
first_fof = 0
fof_step = 1
subsample = 1 #subsample factor to not read in all particles
gas_cmap = None

#just for rotations

rotating = False #rotating image only works with normal/position


#just for 'special' gallery - EXPERIMENTAL AND DOESN'T WORK YET

remake_gallery = True #remake gallery of xsmall images
minitype = 'gas' #type of the miniature images
label_only = False #no minature images if True


#questioning variables

usertype = ""


#questioning functions

def askForUserType():
	'''
	Asks the user for their type and raises an exception if somehow broken. Also accepts 'exit' which
	quits the program with exit code 1
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

def askForImageType():
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



    return object_list

#begin questioning

#ask what type of experience they want

usertype = askForUserType()

size_list = askForImageType()

object_list = askForObjectNumbers()

snap_list = askForSnaps()

#testing variables

print 'Usertype: ', usertype
print 'Size List: ', size_list, type(size_list)
print 'Object List: ', object_list, type(object_list)
print 'Snap List: ', snap_list, type(object_list)
