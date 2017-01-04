# Navigator-traffic_lights

Unfortunately Navigator does not have traffic lights in their maps.
This python script "traffic_lights.py" and the accompanying files create "COUNTRY"-TrafficLights.mca files for you.

I rewrote the script for windows as the last step is the use of DiggerConsole.exe.
The script is currently "not finished" for linux/unix/MacOS X. DiggerConsole works with wine under linux/unix/MacOS X but I did not spend time on it right now (even though I'm an avid linux user and do not even have a windows pc myself).

**What does the script (automatically) do:**</br>
  1. It downloads the country/countries you specify in the top of the script from [download.geofabrik.de](http://download.geofabrik.de/) in the "Protocolbuffer Binary Format".</br>
  2. It converts the downloaded "country".pbf files to .GPX files</br>
  3. These GPX files are fed into DiggerConsole.exe which creates the necessary mca files for you.</br>

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

