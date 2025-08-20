# ScinPho
Installation package to simulate scintillated photons. Default scintillator is N11, parameters can be changed via json file upload to change the scintillator. 

After September 1st, 2025, the author of this package will lose access to the LRZ GitLab, please email at gillec4@mcmaster.ca for any questions!

## Installation 

1. Clone the repository through git
2. Navigate to the project folder (simpackage) 
    cd "folder/path"
3. Type: pip install . 
4. Verify your installation by typing "ScinPho --help" in the terminal 

## Usage 

Using the command line, the sim will generate files containing the coordinates of the scintillated photons, the coordinates of the neutron event source at the scintillator (minus ToF time delay), and a file containing clustering labels for each photon coordinate. 

### Required Commands: 

-e/--events: number of events to simulate 
-n/--noise: number of noisy photons to introduce. These have no source coordinates as they don't come from actual events, and all have the label 0. 

### Optional Commands: 

-c/--cores: number of cores to use (simulation is parallelized). Default is 1. 
-spd/--spacedensity: Density of events in space, no leading zeroes
-td/--timedensity: Density of events in time, from 0-1, needs to be a string with no leading zeroes
-f/--folder: Folder in which to save the datafiles (default is current folder)
-m/--mix: True for mixing the data, False for leaving it in order
-v/--verbose: Showing the photon data in terminal or not
-es/--eventscale: Scaling coefficient for number of photons per event. Default value: 1
-st/--starttime: Starting time for all events. Default is randomly generated 
-sx/--startx: Starting x coordinate for all events. Default is randomly generated 
-sy/--starty: Starting y coordinate for all events. Default is randomly generated 
-df/--datafile: File name for the main file. Other files are created with the same basic name and suffixes (sources, labels). Default naming convention is automatic without this command. 


### Scintillator values (can also be uploaded via .json), defaults are N11 values 
-s/spacesigma: Sigma of the Gaussian distribution of photons in x and y
-jf/--file: Name of json file containing all optional arguments as well as parameters for photon decay distribution and distribution of number of photons per event.
