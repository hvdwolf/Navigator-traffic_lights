# Navigator-traffic_lights

Unfortunately MNF Navigator does not have traffic lights in their maps.
This python script "traffic_lights.py" and the accompanying files create "COUNTRY"-TrafficLights.mca files for you.

I rewrote the script for windows as the last step is the use of DiggerConsole.exe.
The script is currently "not finished" for linux/unix/MacOS X. DiggerConsole works with wine under linux/unix/MacOS X but I did not spend time on it right now (even though I'm an avid linux user and do not even have a windows pc myself).

**What does the script (automatically) do:**</br>
  1. It downloads the country/countries you specify in the top of the script from [download.geofabrik.de](http://download.geofabrik.de/) in the "Protocolbuffer Binary Format".</br>
  2. It converts the downloaded "country".pbf files via a few steps to .csv files</br>
  3. These csv files are fed into DiggerConsole.exe which creates the necessary mca files for you.</br>

**Requirements:**</br>
  1. ("soft" requirement) You need to know how to work in the "CMD" command window in Windows (some people still call this "the dosbox").
  2. This "Navigator-traffic_lights" repository, either downloaded as zip or as git repo.</br>
  3. python for windows: Python can be downloaded from https://www.python.org/downloads/ or you can download the Anaconda python version which comes with a lot of "extra" modules already builtin: https://www.continuum.io/downloads</br>
  4. gpsbabel: This can be downloaded from https://www.gpsbabel.org/</br>
  5. Digger Console: This is a MNF (AFAIK) program bundle and can be downloaded from http://download.mapfactor.com/diger_console_12_2_2.zip</br>

**HowTo:**</br>
  1. If you downloaded these repository as zip, unzip the file.</br>
  2. Open traffic_lights.py in some text editor.</br>
    1. Set the correct path **with** executable for gpsbabel (use forward slashes).</br>
    2. Set the correct path (only path) for DiggerConsole (use forward slashes).</br>
    3. Enable the ```region``` string of your choice. Note: Can only be one single region.</br>
    4. Enable and edit the ```countries``` list belonging to that region. This is a list containing the country name (all in lower case), surrounded by double quotes and separated by a comma. Note: Make sure that all countries belong to the specified region and only enable the countries you need.</br>
  3. Once correctly configured start the python script **from inside** the "Navigator-traffic-lights" folder (or whatever you named that folder) like ```python traffic_lights.py```</br>
  4. Your final mca files can be found in ```<drive>:\<path_to_>\Navigator-traffic-lights\Outputdir```

Note that if you have a lot of countries, and especially the big countries like Germany, France, Russia, Canada, etc, it will take quite some time. The script outputs comments to the terminal to show you what it is currently doing.
Note 2: If you plan on creating all files for every country, your conversion might get stuck 3/4 of Europe as download.geofabrik.de will mention that you have reached "the maximum number of downloads for your ip-address". This will repeat itself for Asia. Simply edit the list and remove the already downloaded.converted countries.

## Countries:
### Europe
albania, andorra, austria, azores, belarus, belgium, bosnia-herzegovina, bulgaria, croatia, cyprus, czech-republic, denmark, estonia, faroe-islands, finland, france, georgia, germany, great-britain, greece, hungary, iceland, ireland-and-northern-ireland, isle-of-man, italy, kosovo, latvia, liechtenstein, lithuania, luxembourg, macedonia, malta, moldova, monaco, montenegro, netherlands, norway, poland, portugal, romania, russia, serbia, slovakia, slovenia, spain, sweden, switzerland, turkey, ukraine

### Russia -> Comes without region
russia

### North-America
**In this case I choose for the USA sub-regions instead of separated states**</br>
canada, greenland, mexico, us-midwest, us-northeast, us-pacific, us-south, us-west

### South-America
argentina, bolivia, brazil, chile, colombia, ecuador, paraguay, peru, suriname, uruguay

### Asia
afghanistan, azerbaijan, bangladesh, cambodia, china, gcc-states, india, indonesia, iran, iraq, israel-and-palestine, japan, jordan, kazakhstan, kyrgyzstan, lebanon, malaysia-singapore-brunei, maldives, mongolia, myanmar, nepal, north-korea, pakistan, philippines, south-korea, sri-lanka, syria, taiwan, tajikistan, thailand, turkmenistan, uzbekistan, vietnam, yemen
