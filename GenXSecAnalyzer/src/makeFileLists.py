# cd ..
# python src/makeFileLists.py Drell-Yan

import os, sys
import StandardModelPhysics

samples = {"Drell-Yan"  :StandardModelPhysics.sampleInfo["Drell-Yan"],
           "ElectroWeak":StandardModelPhysics.sampleInfo["ElectroWeak"],
           "MinimumBias":StandardModelPhysics.sampleInfo["MinimumBias"],
           "QCD"        :StandardModelPhysics.sampleInfo["QCD"],
           "TopPhysics" :StandardModelPhysics.sampleInfo["TopPhysics"],
       }

process = sys.argv[1]
count = 0

for recid in samples[process]:
    try:
        cmd = "cernopendata-client get-file-locations --recid {} --protocol xrootd > fileLists/{}/recid_{}.txt".format(recid, process, recid)
        os.system(cmd)
        count+=1
        #if (count%10==0):
        print("Created {} lists.".format(count))
    except:
        print("Failed to create recid_{}.txt".format(recid))

print("{} {} filelists created.".format(count, sys.argv[1]))
