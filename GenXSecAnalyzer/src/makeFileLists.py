# cd ..
# python src/makeFileLists.py StandardModelPhysics Drell-Yan

import os, sys

section = sys.argv[1]
process = sys.argv[2]

if (section == "StandardModelPhysics"):
    import StandardModelPhysics
    samples = StandardModelPhysics.sampleInfo[process]

if (section == "HiggsPhysics"):
    import HiggsPhysics
    samples = HiggsPhysics.sampleInfo[process]

count = 0
for recid in samples:
    os.system("cernopendata-client get-file-locations --recid {} --protocol xrootd > fileLists/{}/{}/recid_{}.txt".format(recid, section, process, recid))
    count+=1
    if (count%10==0): print("Created {} lists.".format(count))

print("{} file lists created for {} {}.".format(count, section, process))
