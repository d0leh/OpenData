############################################################################################################################################## 
#Looks for the .log files outputted by running the GenXSec Analyzer using calculateXSectionAndFilterEfficiency.sh                            #
#                                                                                                                                            #
# Takes the .log files and extracts the following values and their errors:                                                                   #
#  - total cross sections before matchhing (column name in the output numpy array: 'totX_beforeMat')                                         #
#  - total cross sections after matching ('totX_afterMat')                                                                                   #
#  - matching efficiency ('matchingEff')                                                                                                     #             
#  - filter efficiency (weights) ('filterEff(weights)')                                                                                      #
#  - filter efficiency (event) ('filterEff(event)')                                                                                          #
#  - final total cross section ('totX_final')                                                                                                #
#  - negative weight fraction ('negWeightFrac')                                                                                              #
#  - equivalent luminosity ('equivLumi')                                                                                                     #
# To access errors, append '_err' to the end of the names                                                                                    #
#                                                                                                                                            #
# These information can be accessed by:                                                                                                      #                                                                      #
#  1. Loading numpy array as output = np.load("output_numpy.npy")                                                                            #
#  2. Accessing each catogory using names                                                                                                    #
#	e.g. output["totX_final"] gives the value of the final total cross section                                                           #
#            output["totX_final_err"] gives its error                                                                                        #
##############################################################################################################################################
# To run the script, simply do: python output_to_numpy.py                                                                                    #
# For each sample, it produces a .npy file with the name of the dataset                                                                      #
##############################################################################################################################################

import os
import numpy as np

file_list = [f for f in os.listdir(".") if f.startswith("xsec") and f.endswith(".log")]

dt = {'names':['totX_beforeMat', 'totX_beforeMat_err', 'totX_afterMat', 'totX_afterMat_err', 'matchingEff', 'matchingEff_err', 'filterEff(weights)', 'filterEff(weights)_err', 'filterEff(event)', 'filterEff(event)_err', 'totX_final', 'totX_final_err', 'negWeightFrac', 'negWeightFrac_err', 'equivLumi', 'equivLumi_err'], 
      'formats':[np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64],
      'metadata':{"totX_beforeMat":"Total cross section before matching (pb)",
                  "totX_afterMat":"Total cross section after matching (pb)",
                  "matchingEff":"Matching efficiency",
                  "filterEff(weights)":"Filter efficiency (taking into account weights)",
                  "filterEff(event)":"Filter efficiency (event-level)",
                  "totX_final":"Final cross senction after filter (pb)",
                  "negWeightFrac":"Final fraction of events with negative weights after filter",
                  "equivLumi":"Final equivalent lumi for 1M events (1/fb)",
              }
}

for fname in sorted(file_list):
    xsec_arr = np.zeros(16)
    xsec_arr.dtype=dt
    with open(fname) as f:
        contents = f.read().split("\n")

        try:
            dset = fname.split("xsec_")[-1].split(".")[0] # dataset name

            x_valerr = [c for c in contents if "Before matching: total cross section" in c][0].split("= ")[-1].split() # value
            xsec_arr["totX_beforeMat"]=float(x_valerr[0])
            xsec_arr["totX_beforeMat_err"]=float(x_valerr[2])
            
            x_valerr = [c for c in contents if "After matching: total cross section" in c][0].split("= ")[-1].split()
            xsec_arr["totX_afterMat"]=float(x_valerr[0])
            xsec_arr["totX_afterMat_err"]=float(x_valerr[2])

            x_valerr = [c for c in contents if "Matching efficiency" in c][0].split("= ")[-1].split()
            xsec_arr["matchingEff"]=float(x_valerr[0])
            xsec_arr["matchingEff_err"]=float(x_valerr[2])

            x_valerr = [c for c in contents if "Filter efficiency (taking into account weights)" in c][0].split("= ")[-1].split()
            xsec_arr["filterEff(weights)"]=float(x_valerr[0])
            xsec_arr["filterEff(weights)_err"]=float(x_valerr[2])

            x_valerr = [c for c in contents if "Filter efficiency (event-level)" in c][0].split("= ")[-1].split()
            xsec_arr["filterEff(event)"]=float(x_valerr[0])
            xsec_arr["filterEff(event)_err"]=float(x_valerr[2])

            x_valerr = [c for c in contents if "After filter: final cross section" in c][0].split("= ")[-1].split()
            xsec_arr["totX_final"]=float(x_valerr[0])
            xsec_arr["totX_final_err"]=float(x_valerr[2])

            x_valerr = [c for c in contents if "After filter: final fraction of events with negative weights" in c][0].split("= ")[-1].split()
            xsec_arr["negWeightFrac"]=float(x_valerr[0])
            xsec_arr["negWeightFrac_err"]=float(x_valerr[2])

            x_valerr  = [c for c in contents if "final equivalent lumi for 1M events (1/fb)" in c][0].split("= ")[-1].split()
            xsec_arr["equivLumi"]=float(x_valerr[0])
            xsec_arr["equivLumi_err"]=float(x_valerr[2])
        except:
	    print("Save to numpy failed {}".format(fname))

    np.save(dset, xsec_arr)
    #print(xsec_arr)
    #print(xsec_arr["equivLumi"])

    #print(xsec_arr.dtype.metadata)
    #print(xsec_arr.dtype.metadata["equivLumi"])
    
