#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 1.0, 201607, Harry van der Wolf
# Version 1.1, 201701, Harry van der Wolf; 
		#urllib -> do not read large files into memory but write in chunks to disk; 
		#Create all mca files directly from the script.

import os, sys, platform, subprocess, shutil


if sys.version_info<(3,0,0):
	# Fall back to Python 2's urllib2
	from urllib2 import urlopen
else:
	# For Python 3.0 and later
	from urllib.request import urlopen

# Use dictionary for our variables, makes it easier to structure this script into functions (if I feel it is necessary :) )
var_dirs = {}

###################################################
###################################################

# Between the double lines you need to modify some data. Outside is not necessary
# These two lines are for windows. Note: Even on windows you need to use FORWARD slashes
var_dirs['gpsbabel'] = "C:/Program Files (x86)/GPSBabel/gpsbabel.exe"
var_dirs['DIGGERPATH'] = "C:/Users/387640/Downloads/digger_console"

# europe or north-america, asia, south-america, africa, australia-oceania, central-america
# enable one region and one set of countries per run
### Europe
# Note: Even though the script allows you to download and process all countris of europe in one go, I had to do it in 3 times.
# Simply because the download.geofabrik.de server stopped me after a number of countries with "too many requests in this 
# time period from this user"
region = "europe"
countries = ["albania", "andorra", "austria", "azores", "belarus", "belgium", "bosnia-herzegovina", "bulgaria", "croatia", "cyprus", "czech-republic", "denmark", "estonia", "faroe-islands", "finland", "france", "georgia", "germany", "great-britain", "greece", "hungary", "iceland", "ireland-and-northern-ireland", "isle-of-man", "italy", "kosovo", "latvia", "liechtenstein", "lithuania", "luxembourg", "macedonia", "malta", "moldova", "monaco", "montenegro", "netherlands", "norway", "poland", "portugal", "romania", "russia", "serbia", "slovakia", "slovenia", "spain", "sweden", "switzerland", "turkey", "ukraine"]

### Russia" -> Comes without region
#region = ""
#countries = ["russia"]

### North-America
#region="north-america"
# In this case I choose for the USA sub-regions instead of separated states
#countries = ["canada", "greenland", "mexico", "us-midwest", "us-northeast", "us-pacific", "us-south", "us-west"]

### South-America
#region = "south-america"
#countries = ["argentina", "bolivia", "brazil", "chile", "colombia", "ecuador", "paraguay", "peru", "suriname", "uruguay"]

### Asia
#region = "asia"
#countries = ["afghanistan", "azerbaijan", "bangladesh", "cambodia", "china", "gcc-states", "india", "indonesia", "iran", "iraq", "israel-and-palestine", "japan", "jordan", "kazakhstan", "kyrgyzstan", "lebanon", "malaysia-singapore-brunei", "maldives", "mongolia", "myanmar", "nepal", "north-korea", "pakistan", "philippines", "south-korea", "sri-lanka", "syria", "taiwan", "tajikistan", "thailand", "turkmenistan", "uzbekistan", "vietnam", "yemen"]

# small test country
#region = "europe"
#countries = ["luxembourg"]


# Below these double hashtags line you should not have to change anything
###################################################
###################################################

######################################################################
# Now create some base directories and the variables for it
var_dirs['CUR_DIR'] = os.path.dirname(os.path.abspath(__file__))
var_dirs['WORKDIR'] = os.path.join(var_dirs['CUR_DIR'], "Workdir")
if not os.path.exists(var_dirs['WORKDIR']):
    os.mkdir(var_dirs['WORKDIR'])
var_dirs['OutputDir'] = os.path.join(var_dirs['CUR_DIR'], "OutputDir")
if not os.path.exists(var_dirs['OutputDir']):
    os.mkdir(var_dirs['OutputDir'])

# set for windows
var_dirs['DIGGER'] = os.path.join(var_dirs['DIGGERPATH'], "DiggerConsole.exe")
var_dirs['TOOLDIR'] = os.path.join(var_dirs['CUR_DIR'], "tools")

OSplatform = platform.system()
for country in countries:
	print("\n\n== Downloading and processing " + country + " ==")
	print("\n== Downloading")
	map_url = "http://download.geofabrik.de/" + region + "/" + country + "-latest.osm.pbf"
	mapfile = urlopen( map_url )
	filesprefix = os.path.join(var_dirs['WORKDIR'], country)
	with open( filesprefix + "-latest.osm.pbf", 'wb') as output:
		while True:
			tmp = mapfile.read(1024)
			if not tmp:
				break
			output.write(tmp)

	print("\n== Converting " + country + " to .o5m format")
	if OSplatform == "Windows":
		os.system(os.path.join(var_dirs['TOOLDIR'], "osmconvert.exe") + " -v " + filesprefix + "-latest.osm.pbf" + " --drop-author --out-o5m -o=" + filesprefix + "-latest.o5m")
	else:
		os.system("osmconvert -v " + filesprefix + "-latest.osm.pbf" + " --drop-author --out-o5m > " + filesprefix + "-latest.o5m")
	print("\n\n== Filtering the traffic signals out of " + country + " ==")
	# on any pc/server with more than 2GB memory remove the --hash-memory=400-50-2 parameter
	if OSplatform == "Windows":
		os.system(os.path.join(var_dirs['TOOLDIR'], "osmfilter.exe") + " " + filesprefix + "-latest.o5m" + " --hash-memory=400-50-2 --parameter-file=" + os.path.join(var_dirs['CUR_DIR'], 'traffic_signals.txt') + " -o=" + filesprefix + "-latest.osm")
	else:
		os.system("osmfilter " + filesprefix + "-latest.o5m" + "	--hash-memory=400-50-2 --parameter-file=traffic_signals.txt	> " + filesprefix + "-latest.osm")
	print("\n\n== run gpsbabel on our country filtered osm file to convert to gpx ==")
	if OSplatform == "Windows":
		os.system('"' + var_dirs['gpsbabel'] + '"' + " -i osm -f " + filesprefix + "-latest.osm -o gpx -F " + filesprefix + "-latest.gpx")
		#subprocess.call(gpsbabel + " -i osm -f " + country + "-latest.osm -o gpx -F " + country + "-latest.gpx")
	else:
		os.system("gpsbabel -i osm -f " + filesprefix + "-latest.osm -o gpx -F " + filesprefix + "-latest.gpx")


	print("\n\n== Remove some unneccessary lines ==")
	useless_words = ["cmt", "desc"] # actually useless lines containing these words
	with open(filesprefix + "-latest.gpx") as oldfile, open(filesprefix + "-TrafficSignals.gpx", "a") as newfile:
		for line in oldfile:
			if not any(useless_word in line for useless_word in useless_words):
				newfile.write(line)

	print("== Removing our downloaded files and intermediate files to clean up")
	os.remove(filesprefix + "-latest.osm.pbf")
	os.remove(filesprefix + "-latest.osm")
	os.remove(filesprefix + "-latest.o5m")
	os.remove(filesprefix + "-latest.gpx")
	
	print("###############################################")
	print("== Now creating the mca file")
	# Create tmp dir for digger_config and gpx
	TMPworkDir = os.path.join(var_dirs['CUR_DIR'], country.upper() + "-TrafficSignals")
	if not os.path.exists(TMPworkDir):
		os.mkdir(TMPworkDir)
	shutil.copyfile(filesprefix + "-TrafficSignals.gpx", os.path.join(TMPworkDir, country.upper() + "-TrafficSignals.gpx"))
	# Create digger_config file
	f = open(os.path.join(var_dirs['CUR_DIR'],"basic_digger_config.xml"),'r')
	filedata = f.read()
	f.close()
	newdata = filedata.replace("COUNTRY", country.upper())
	newdata = newdata.replace("WORKDIR", var_dirs['WORKDIR'].replace('\\', '/'))
	newdata = newdata.replace("CUR_DIR", var_dirs['CUR_DIR'].replace("\\","/"))
	f = open(os.path.join(TMPworkDir, "digger_config.xml"),'w')
	f.write(newdata)
	f.close()	
	
	# Switch to digger console directory
	os.chdir(var_dirs['DIGGERPATH'])
	print("== Calling diggerconsole to create the mca")
	# do a simple system call
	os.system(var_dirs['DIGGER'] + " " + os.path.join(TMPworkDir, "digger_config.xml"))
	# copy mca to output folder
	shutil.move(os.path.join(var_dirs['CUR_DIR'], country.upper() + "-TrafficSignals.mca"), os.path.join(var_dirs['OutputDir'], country.upper() + "-TrafficSignals.mca"))

print("\n\n###############################################")
print("###############################################")
print("Your mca file(s) should now be available in " + var_dirs['OutputDir'])
