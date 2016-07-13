#!/bin/bash

# bash file to extract traffic signals from osm files
# version 0.1, Harry van der Wolf, 20150416
# requirements: wget, gpsbabel, osmconvert, osmfilter

region="europe"    # or north-america, asia, south-america, africa, australia-oceania, central-america
countries="austria belgium czech-republic denmark finland france germany great-britain greece hungary ireland-and-northern-ireland italy luxembourg netherlands norway poland portugal spain sweden switzerland t$

# test country
#countries="luxembourg"

for country in $countries
do
  printf "Downloading and processing $country\n\n"
  wget download.geofabrik.de/$region/$country-latest.osm.pbf -O $country-latest.osm.pbf
  printf "Converting $country to .o5m format\n"
  osmconvert -v $country-latest.osm.pbf --drop-author --out-o5m > $country-latest.o5m
  printf "Filtering the traffic signals out of $country\n"
  # on any pc/server with more than 2GB memory remove the --hash-memory=400-50-2 parameter
  osmfilter $country-latest.o5m  --hash-memory=400-50-2 --parameter-file=traffic_signals.txt  > $country-latest.osm
  printf "run gpsbabel on our $country filtered osm file to convert to gpx\n"
  gpsbabel -i osm -f $country-latest.osm -o gpx -F $country-latest.gpx
  printf "Remove some unneccessary lines\n"
  cat $country-latest.gpx | grep -v "cmt" | grep -v "desc" > $country-TrafficSignals.gpx
  printf "Removing our downloaded files and intermediate files to clean up"
  rm $country-latest.o* $country-latest.gpx
done

printf "You should now have your gpx file(s) ready. Run them through digger"
