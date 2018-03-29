#! /usr/bin/env python
import subprocess

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

#Classification categories text file


#Detection categories text file


# CONFIG PARAMETERS:
#	SITE_NAME -> where should we pull our google images from
#	OUTPUT_DIRECTORY -> where we should save our images
#	CLASSIFICATION_FILE -> text file that holds classification categories	
#	CLASSIFICATION_LIMIT -> number of images to pull for each classification category
#	DETECTION_FILE -> text file that holds detection categories
#	DETECTION_LIMIT -> number of images to pull for each detection category

SITE_NAME = "https://www.flickr.com"
OUTPUT_DIRECTORY = "flickr_images"
CLASSIFICATION_FILE = "imgnet_classify_categories.txt" 
CLASSIFICATION_LIMIT = "1"
DETECTION_FILE = "imgnet_detection_categories.txt"
DETECTION_LIMIT = "1"


#read in each line of file that holds classification categories
with open(CLASSIFICATION_FILE, "r") as fin:
	dirty_classification = [((line[10:-1]).split(",")) for line in fin]
	classification_categories = [[item.strip() for item in category] for category in dirty_classification]

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
#	10 images for each classification category
#	20 images for each detection category
# NOTE_:
#	Not sure how to handle when one category has multiple
#	descriptions for the same thing... For now I am going
#	to only use the first descriptive name for each category

#downloading classification categories
for category in classification_categories:
	subprocess.call(["googleimagesdownload", "--keywords", category[0], "--specific_site", SITE_NAME, "--limit", CLASSIFICATION_LIMIT, "-o", "flickr_images"])
	
#downloading detection categories
#for category in detection_categories:
#	subprocess.call(["googleimagesdownload", "--keywords", category[0], "--specific_site", SITE_NAME, "--limit", DETECTION_LIMIT])


