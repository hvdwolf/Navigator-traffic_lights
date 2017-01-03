#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 1.0, 201607, Harry van der Wolf

import os, sys, platform, subprocess
if sys.version_info<(3,0,0):
	# Fall back to Python 2's urllib2
	from urllib2 import urlopen
else:
	# For Python 3.0 and later
	from urllib.request import urlopen


# set for windows
gpsbabel = "C:\Program Files (x86)\GPSBabel\gpsbabel.exe"
# 

region = "europe"		# or north-america, asia, south-america, africa, australia-oceania, central-america
countries = ["austria", "belgium", "czech-republic", "denmark", "finland", "france", "germany", "great-britain", "hungary", "ireland-and-northern-ireland", "italy", "luxembourg", "netherlands", "norway", "poland", "portugal", "spain", "sweden", "switzerland"]
### "greece",  -> Greece currently doesn work due to unicode characters. Need to checkthat sometime

# test country
#countries = ["luxembourg", "belgium"]

OSplatform = platform.system()
for country in countries:
	print("\n\n== Downloading and processing " + country + " ==")
	print("\n== Downloading")
	map_url = "http://download.geofabrik.de/" + region + "/" + country + "-latest.osm.pbf"
	mapfile = urlopen( map_url )
	with open( country + "-latest.osm.pbf", 'wb') as output:
		while True:
			tmp = file.read(1024)
			if not tmp:
				break
			output.write(tmp)

	print("\n== Converting " + country + " to .o5m format")
	os.system("osmconvert -v " + country +"-latest.osm.pbf --drop-author --out-o5m > " + country + "-latest.o5m")
	print("\n\n== Filtering the traffic signals out of " + country + " ==")
	# on any pc/server with more than 2GB memory remove the --hash-memory=400-50-2 parameter
	os.system("osmfilter " + country + "-latest.o5m	--hash-memory=400-50-2 --parameter-file=traffic_signals.txt	> " + country + "-latest.osm")
	print("\n\n== run gpsbabel on our country filtered osm file to convert to gpx ==")
	if OSplatform == "Windows":
		os.system('"' + gpsbabel + '"' + " -i osm -f " + country + "-latest.osm -o gpx -F " + country + "-latest.gpx")
		#subprocess.call(gpsbabel + " -i osm -f " + country + "-latest.osm -o gpx -F " + country + "-latest.gpx")
	else:
		os.system("gpsbabel -i osm -f " + country + "-latest.osm -o gpx -F " + country + "-latest.gpx")


	print("\n\n== Remove some unneccessary lines ==")
	useless_words = ["cmt", "desc"] # actually useless lines containing these words
	with open(country + "-latest.gpx") as oldfile, open(country + "-TrafficSignals.gpx", "a") as newfile:
		for line in oldfile:
			if not any(useless_word in line for useless_word in useless_words):
				newfile.write(line)

	print("Removing our downloaded files and intermediate files to clean up")
	os.remove(country + "-latest.osm.pbf")
	os.remove(country + "-latest.osm")
	os.remove(country + "-latest.o5m")
	os.remove(country + "-latest.gpx")

print("You should now have your gpx file(s) ready. Run them through digger")
