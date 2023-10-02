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

count = 0

for recid in samples[sys.argv[1]]:
    try:
        cmd = "cernopendata-client get-file-locations --recid {} --protocol xrootd > fileLists/recid_{}.txt".format(recid, recid)
        os.system(cmd)
        count+=1
    except:
        print("Failed to create recid_{}.txt".format(recid))

print("{} {} filelists created.".format(count, sys.argv[1]))
