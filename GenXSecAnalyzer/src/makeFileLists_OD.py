# cd ..
# python src/makeFileLists.py 2015 StandardModelPhysics Drell-Yan

import os, sys

year = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]

if year == "2015":
    if (section == "StandardModelPhysics"):
        import StandardModelPhysics2015
        samples = StandardModelPhysics2015.sampleInfo[process]

    if (section == "HiggsPhysics"):
        import HiggsPhysics2015
        samples = HiggsPhysics2015.sampleInfo[process]

count = 0
outdir = "fileLists/{}/{}/{}".format(year, section, process)
for recid in samples:
    os.system("echo {} > {}/{}.txt".format(samples[recid], outdir, recid))
    os.system("cernopendata-client get-file-locations --recid {} --protocol xrootd >> {}/{}.txt".format(recid, outdir, recid))
    count+=1
    if (count%10==0): print("Created {} lists.".format(count))

print("{} file lists created for {} {}.".format(count, section, process))
