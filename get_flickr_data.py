#! /usr/bin/env python
import subprocess
import pprint

#########################################################
# pip install google_images_download			#
#	-open source on github as well			#
# Use like the following (one line):			#
#	>googleimagesdownload 				#	
#	>	--keywords "exampleCategory"		#
#	>	--specific_site "exampleURL"		#
# for more usage information look at			#
# "https://github.com/hardikvasa/google-images-download"#
#########################################################								


# CONFIG PARAMETERS:
#	SITE_NAME -> where should we pull our google images from
#	CLASSIFICATION_FILE -> text file that holds classification categories	
#	CLASSIFICATION_LIMIT -> number of images to pull for each classification category
#	CLASSIFICATION_OUTPUT_DIRECTORY -> directory to save classification images
#	DETECTION_FILE -> text file that holds detection categories
#	DETECTION_LIMIT -> number of images to pull for each detection category
#	DETECTION_OUTPUT_DIRECTORY -> directory to save detection images

TIME = '{"time_min":"01/01/2017","time_max":"04/01/2018"}'
SITE_NAME = "https://www.flickr.com"
CLASSIFICATION_FILE = "imgnet_classify_categories.txt" 
CLASSIFICATION_LIMIT = "25"
CLASSIFICATION_OUTPUT_DIRECTORY = ["classification_flickr_images/dan", "classification_flickr_images/jisoo", "classification_flickr_images/jiancheng", "classification_flickr_images/ruhana", "classification_flickr_images/nobelle"]
DETECTION_FILE = "imgnet_detection_categories.txt"
DETECTION_LIMIT = "1"
DETECTION_OUTPUT_DIRECTORY = "detection_flickr_images"


#read in each line of file that holds classification categories
with open(CLASSIFICATION_FILE, "r") as fin:
	classification_categories = [((line[:-1]).strip().split(",")) for line in fin]
	classification_categories = [[line.strip() for line in category] for category in classification_categories]

#read in each line of file that holds detection categories
with open(DETECTION_FILE, "r") as fin:
	detection_categories = [(line[:-1].strip().replace(" or ",",").split(",")) for line in fin]

# '*_categories' holds a cleaned List of all categories 
# EX:
#	[	
#		['great white shark', 'white shark', 'man-eater', 'man-eating shark', 'Carcharodon carcharias'], 
#		['goldfish', 'Carassius auratus'], 
#		['hen'], ['vulture']
#	]

#following commands to download: 
#	CLASSIFICATION_LIMIT images for each classification category
#	DETECTION_LIMIT images for each detection category
# NOTE_:
#	Not sure how to handle when one category has multiple
#	descriptions for the same thing... For now I am going
#	to only use the first descriptive name for each category

#downloading classification categories
counter = 0
i = 0
for category in classification_categories:
	if(counter < 250):
		i = 0
	elif(counter >= 250 and counter < 500):
		i = 1
	elif(counter >= 500 and counter < 750):
		i = 2
	elif(counter >=750):
		i = 3
	subprocess.call(["googleimagesdownload", "--keywords", category[0], "--specific_site", SITE_NAME, "--limit", CLASSIFICATION_LIMIT, "--time_range", TIME, "-o", CLASSIFICATION_OUTPUT_DIRECTORY[i]])
	counter+=1
	
#downloading detection categories
#for category in detection_categories:
#	subprocess.call(["googleimagesdownload", "--keywords", category[i][0], "--specific_site", SITE_NAME, "--limit", DETECTION_LIMIT, "-o", DETECTION_OUTPUT_DIRECTORY])

