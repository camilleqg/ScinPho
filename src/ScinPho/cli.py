import argparse
from .sim import new_parallel_sim

def main():
    parser = argparse.ArgumentParser(prog = "ScinPho", description="Neutron event simulator")

#def sim(events, noise, scramble, verbose = False, eventscale=1, noisescale=1, spacesigma=0.00021233045007200478, start_time=-1, start_x=-1, start_y=-1, dataSaveID = None, file=None):
    parser.add_argument("-e", "--events", type = int, required=True, help="Number of neutron events to simulate")
    parser.add_argument("-c", "--cores", type=int, default=1, help="Number of cores to be used, default is 1 (non parallelized)")
    parser.add_argument("-n", "--noise", type = int, required = True, help="Number of noise photons to include in the data")
    parser.add_argument("-spd", "--spacedensity", type = str, default = '1', help="Density of events in time, from 0-1, needs to be a string with no leading zeroes")
    parser.add_argument("-td", "--timedensity", type = str, default = '1', help = "Density of events in space, scales the detector sidelength, no leading zeroes")
    parser.add_argument("-f", "--folder", type =str, default = None, help = "Folder in which to save the datafiles.")
    parser.add_argument("-m", "--mix", type = bool, default=False, help="True for mixing the data, False for leaving it in order")
    parser.add_argument("-v", "--verbose", type = str, default = False, help="Showing the photon data in terminal or not")
    parser.add_argument("-es", "--eventscale", type = float, default = 1, help = "Scaling coefficient for number of photons per event. Default value: 1")
    parser.add_argument("-s", "--spacesigma", type = float, default = 0.00021233045007200478, help = "Sigma of the Gaussian distribution of photons in x and y. Default value: 0.00021233045007200478")
    parser.add_argument("-st", "--starttime", type = float, default = -1, help = "Start time for all events. Default value is randomly generated.")
    parser.add_argument("-sx", "--startx", type = float, default = -1, help = "Starting x coordinate for all events. Default value is randomly generated.")
    parser.add_argument("-sy", "--starty", type = float, default = -1, help = "Starting y coordinate for all events. Default value is randomly generated.")
    parser.add_argument("-df", "--datafile", type = str, default = None, help = "Text file name for saving data. Truth file will have the same name but prefixed with truth_")
    parser.add_argument("-jf", "--file", type = None, default = None, help = "Name of json file containing all optional arguments as well as parameters for photon decay distribution and distribution of number of photons per event.")

    args = parser.parse_args()

    if args.events:
        new_parallel_sim(events=args.events, noise=args.noise, num_cores=args.cores, sp_density=args.spacedensity, t_density=args.timedensity, folder=args.folder, mix=args.mix, verbose=args.verbose, eventscale=args.eventscale, spacesigma=args.spacesigma, start_time=args.starttime, start_x=args.startx, start_y=args.starty, dataSaveID=args.datafile, file=args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()