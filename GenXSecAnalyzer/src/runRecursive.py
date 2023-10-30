# cd ..
# python runRecursive.py StandardModelPhysics Drell-Yan

import os, sys

section = sys.argv[1]
process = sys.argv[2]
skipexisting = False

if (section == "StandardModelPhysics"):
    import StandardModelPhysics
    samples = {"Drell-Yan"  :StandardModelPhysics.sampleInfo["Drell-Yan"],
               "ElectroWeak":StandardModelPhysics.sampleInfo["ElectroWeak"],
               "MinimumBias":StandardModelPhysics.sampleInfo["MinimumBias"],
               "QCD"        :StandardModelPhysics.sampleInfo["QCD"],
               "TopPhysics" :StandardModelPhysics.sampleInfo["TopPhysics"],
           }

if (section == "HiggsPhysics"):
    import HiggsPhysics
    samples = {"BeyondStandardModel": HiggsPhysics.sampleInfo["BeyondStandardModel"],
               "StandardModel": HiggsPhysics.sampleInfo["StandardModel"],
    }

count = 0
for recid in samples[process]:
    #cmd = "./src/calculateXSectionAndFilterEfficiency.sh -f recid_{}.txt -s {} -p {} -n 10000000".format(recid, section, process)
    cmd = "./src/calculateXSectionAndFilterEfficiency.sh -f recid_{}.txt -s {} -p {} -n 1".format(recid, section, process)
    print(cmd)
    os.system(cmd)
    count+=1
    print("Processed {} samples.".format(count))
    
print("Finished running all the samples.")    
