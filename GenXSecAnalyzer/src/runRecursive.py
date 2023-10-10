# cd ..
# python runRecursive.py Drell-Yan

import os, sys
import StandardModelPhysics

samples = {"Drell-Yan"  :StandardModelPhysics.sampleInfo["Drell-Yan"],
           "ElectroWeak":StandardModelPhysics.sampleInfo["ElectroWeak"],
           "MinimumBias":StandardModelPhysics.sampleInfo["MinimumBias"],
           "QCD"        :StandardModelPhysics.sampleInfo["QCD"],
           "TopPhysics" :StandardModelPhysics.sampleInfo["TopPhysics"],
       }

skipexisting = False

process = sys.argv[1]
count = 0

for recid in samples[process]:
    cmd = "./src/calculateXSectionAndFilterEfficiency.sh -f fileLists/{}/recid_{}.txt -d {} -n 10000000 -s {}".format(process, recid, process, skipexisting)
    print(cmd)
    os.system(cmd)
    count+=1
    print("Processed {} samples.".format(count))
    
print("Finished running all the samples.")    
