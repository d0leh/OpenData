# cd ..
# python src/makeFileLists.py 2015 StandardModelPhysics Drell-Yan

import os, sys

year = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]

if (section == "StandardModelPhysics"):
    import StandardModelPhysics2015
    samples = StandardModelPhysics2015.sampleInfo[process]

if (section == "HiggsPhysics"):
    import HiggsPhysics2015
    samples = HiggsPhysics2015.sampleInfo[process]

count = 0
for recid in samples:
    os.system("cernopendata-client get-file-locations --recid {} --protocol xrootd > fileLists/{}/{}/{}/{}.txt".format(recid, year, section, process, recid))
    count+=1
    if (count%10==0): print("Created {} lists.".format(count))

print("{} file lists created for {} {}.".format(count, section, process))
