# Navigator-traffic_lights

Unfortunately Navigator does not have traffic lights in their maps.
This python script "traffic_lights.py" and the accompanying files create "COUNTRY"-TrafficLights.mca files for you.

I rewrote the script for windows as the last step is the use of DiggerConsole.exe.
It is currently "not finished" for linux/unix/MacOS X. DiggerConsole works with wine under linux/unix/MacOS X but I did not spend time on it right now.

**What does it do:**</br>
  1. It downloads the country/countries you specify in the top of the script from download.geofabrik.de in the "Protocolbuffer Binary Format".</br>
  2. It converts the downloaded "country".pbf files to .GPX files</br>
  3. These GPX files are fed into DiggerConsole.exe which creates the necessary mca files for you.</br>

**Requirements:**</br>
  1. This repository, either downloaded as zip or as git repo.</br>
  2. python for windows: That can be downloaded from https://www.python.org/downloads/ or you can download the Anaconda python version which comes with a lot of "extra" modules already builtin: https://www.continuum.io/downloads</br>
  3. gpsbabel: This can be downloaded from https://www.gpsbabel.org/</br>
  4. Digger Console: This can be downloaded from http://download.mapfactor.com/diger_console_12_2_2.zip</br>

**HowTo:**</br>
  1. If you downloaded these repository as zip, unzip the file.</br>
  2. Open traffic_lights.py in some text editor.</br>
    1. Edit the REGION string and add your Region. Note: Can only be one region.</br>
    2. Edit the countries list. This is a list containing the country name all in lower case, surrounded by double quotes and separated by a comma.</br>
    3. Set the correct path **with** executable for gpsbabel (use forward slashes).</br>
    4. Set the correct path for DiggerConsole (use forward slashes).</br>
  3. Once correctly configured start the python script **from inside** the "Navigator-traffic-lights" folder (or whatever you named that folder) like ```python traffic_lights.py```</br>
  4. Your final mca files can be found in ```<drive>:\<path_to_>\Navigator-traffic-lights\Outputdir```
