# cd ..
# python runRecursive.py StandardModelPhysics Drell-Yan

import os, sys

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]
skipexisting = False

if (section == "StandardModelPhysics"):
    import StandardModelPhysics
    samples = StandardModelPhysics.sampleInfo[process]

if (section == "HiggsPhysics"):
    import HiggsPhysics
    samples = HiggsPhysics.sampleInfo[process]

count = 0
for sample in samples:
    sample_name = 
    cmd = "./src/calculateXSectionAndFilterEfficiency.sh -f {}.txt -s {} -p {} -n 10000000 -k {}".format(recid, section, process, skipexisting)
    print(cmd)
    os.system(cmd)
    count+=1
    print("Processed {} samples.".format(count))
    
print("Finished running all the samples.")    
