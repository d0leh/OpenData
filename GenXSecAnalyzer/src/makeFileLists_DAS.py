# cd ..
# python src/makeFileLists.py 2016 StandardModelPhysics Drell-Yan

# dasgoclient -query="child dataset=/DY1JetsToLL_M-10to50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM"

import os, sys

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]

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
