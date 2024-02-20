# cd ..
# python runRecursive_OD.py 2015 StandardModelPhysics Drell-Yan

import os, sys

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]
skipexisting = False

if year == "2015":
    if (section == "StandardModelPhysics"):
        import StandardModelPhysics2015
        samples = StandardModelPhysics2015.sampleInfo[process]
    if (section == "HiggsPhysics"):
        import HiggsPhysics2015
        samples = HiggsPhysics2015.sampleInfo[process]

count = 0
for recid in samples:
    #sample_name = samples[recid].split('/')[1]
    cmd = "./src/calculateXSectionAndFilterEfficiency.sh -f {} -y {} -s {} -p {} -n 10000000 -k {}".format(recid, year, section, process, skipexisting)
    print(cmd)
    os.system(cmd)
    count+=1
    print("Processed {} samples.".format(count))
    
print("Finished running all the samples.")    
