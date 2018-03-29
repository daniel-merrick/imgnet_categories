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


# CONFIG PARAMETERS:
#	SITE_NAME -> where should we pull our google images from
#	CLASSIFICATION_FILE -> text file that holds classification categories	
#	CLASSIFICATION_LIMIT -> number of images to pull for each classification category
#	CLASSIFICATION_OUTPUT_DIRECTORY -> directory to save classification images
#	DETECTION_FILE -> text file that holds detection categories
#	DETECTION_LIMIT -> number of images to pull for each detection category
#	DETECTION_OUTPUT_DIRECTORY -> directory to save detection images

SITE_NAME = "https://www.flickr.com"
CLASSIFICATION_FILE = "imgnet_classify_categories.txt" 
CLASSIFICATION_LIMIT = "1"
CLASSIFICAITON_OUTPUT_DIRECTORY = "classification_flickr_images"
DETECTION_FILE = "imgnet_detection_categories.txt"
DETECTION_LIMIT = "1"
DETECTION_OUTPUT_DIRECTORY = "detection_flickr_images"


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
#	CLASSIFICATION_LIMIT images for each classification category
#	DETECTION_LIMIT images for each detection category
# NOTE_:
#	Not sure how to handle when one category has multiple
#	descriptions for the same thing... For now I am going
#	to only use the first descriptive name for each category

#downloading classification categories
for category in classification_categories:
	subprocess.call(["googleimagesdownload", "--keywords", category[0], "--specific_site", SITE_NAME, "--limit", CLASSIFICATION_LIMIT, "-o", "CLASSIFICATION_OUTPUT_DIRECTORY"])
	
#downloading detection categories
for category in detection_categories:
	subprocess.call(["googleimagesdownload", "--keywords", category[0], "--specific_site", SITE_NAME, "--limit", DETECTION_LIMIT, "-o", DETECTION_OUTPUT_DIRECTORY])


