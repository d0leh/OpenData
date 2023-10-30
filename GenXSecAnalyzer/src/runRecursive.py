# cd ..
# python runRecursive.py StandardModelPhysics Drell-Yan

import os, sys

section = sys.argv[1]
process = sys.argv[2]
skipexisting = False

if (section == "StandardModelPhysics"):
    import StandardModelPhysics
    samples = StandardModelPhysics.sampleInfo[process]

if (section == "HiggsPhysics"):
    import HiggsPhysics
    samples = HiggsPhysics.sampleInfo[process]

count = 0
for recid in samples:
    cmd = "./src/calculateXSectionAndFilterEfficiency.sh -f recid_{}.txt -s {} -p {} -n 10000000 -k {}".format(recid, section, process, skipexisting)
    print(cmd)
    os.system(cmd)
    count+=1
    print("Processed {} samples.".format(count))
    
print("Finished running all the samples.")    
