# OpenData
GenXSecAnalyzer for OpenData
Takes a list files (.txt) and outputs the interesting values as a numpy array by one single command line.

### To get everything we need:
Run ./calculateXSectionAndFilterEfficiency.sh -f <list_of_root_files.txt> -d <name_of_the_dataset/process> -n <maximum_num_of_events> 
e.g.: ./calculateXSectionAndFilterEfficiency.sh -f DYJetsToLL.txt -d DYJetsToLL -n 10000
Set maximum number of events to -1 to run all the events in each root file

### Understanding outputs
One .log file and one .npy file for each input filelist
The .npy file is automatically generated from the .log file

To use the output of the GenXSecAnalyzer, we only need to do:
import numpy as np

result = np.load("<dataset_name>.npy")

To check all the metadata:
print(result.dtype.metadata)

To check the metadata for a specific column:
print(xsec_arr.dtype.metadata["<column_name>"])
e.g.: print(xsec_arr.dtype.metadata["equivLumi"])
