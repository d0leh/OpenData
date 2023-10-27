# cd ..
# python src/makeFileLists.py StandardModelPhysics Drell-Yan

import os, sys

section = sys.argv[1]
process = sys.argv[2]

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
    samples = {#"BeyondStandardModel": HiggsPhysics.sampleInfo["BeyondStandardModel"],
               "StandardModel": HiggsPhysics.sampleInfo["StandardModel"],
}

count = 0

for recid in samples[process]:
    try:
        cmd = "cernopendata-client get-file-locations --recid {} --protocol xrootd > fileLists/{}/{}/recid_{}.txt".format(recid, section, process, recid)
        os.system(cmd)
        count+=1
        if (count%10==0):
            print("Created {} lists.".format(count))
    except:
        print("Failed to create recid_{}.txt".format(recid))

print("{} {} filelists created.".format(count, process))
