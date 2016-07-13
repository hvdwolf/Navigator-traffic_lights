#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 1.0, 201607, Harry van der Wolf

import os, sys, platform, urllib2


region = "europe"		# or north-america, asia, south-america, africa, australia-oceania, central-america
countries = ["austria", "belgium", "czech-republic", "denmark", "finland", "france", "germany", "great-britain", "greece", "hungary", "ireland-and-northern-ireland", "italy", "luxembourg", "netherlands", "norway", "poland", "portugal", "spain", "sweden", "switzerland"]

# test country
#countries = ["luxembourg", "belgium"]

for country in countries:
	print("\n\n== Downloading and processing " + country + " ==")
	print("\n== Downloading")
	map_url = "http://download.geofabrik.de/" + region + "/" + country + "-latest.osm.pbf"
	mapfile = urllib2.urlopen( map_url )
	with open( country + "-latest.osm.pbf", 'wb') as output:
		output.write(mapfile.read())

	print("\n== Converting " + country + " to .o5m format")
	os.system("osmconvert -v " + country +"-latest.osm.pbf --drop-author --out-o5m > " + country + "-latest.o5m")
	print("\n\n== Filtering the traffic signals out of " + country + " ==")
	# on any pc/server with more than 2GB memory remove the --hash-memory=400-50-2 parameter
	os.system("osmfilter " + country + "-latest.o5m	--hash-memory=400-50-2 --parameter-file=traffic_signals.txt	> " + country + "-latest.osm")
	print("\n\n== run gpsbabel on our country filtered osm file to convert to gpx ==")
	os.system("gpsbabel -i osm -f " + country + "-latest.osm -o gpx -F " + country + "-latest.gpx")


	print("\n\n== Remove some unneccessary lines ==")
	useless_words = ["cmt", "desc"] # actually useless lines containing these words
	with open(country + "-latest.gpx") as oldfile, open(country + "-TrafficSignals.gpx", "a") as newfile:
		for line in oldfile:
			if not any(useless_word in line for useless_word in useless_words):
				newfile.write(line)

	print("Removing our downloaded files and intermediate files to clean up")
	os.remove(country + "-latest.osm")
	os.remove(country + "-latest.o5m")
	os.remove(country + "-latest.gpx")

print("You should now have your gpx file(s) ready. Run them through digger")
