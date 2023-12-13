# cd ..
# python src/makeFileLists.py 2016 StandardModelPhysics Drell-Yan

# dasgoclient -query="child dataset=/DY1JetsToLL_M-10to50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM"

import os, sys

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]

prefix = "root://cmsxrootd.fnal.gov/"

if (section == "StandardModelPhysics"):
    import StandardModelPhysics2016
    samples = StandardModelPhysics2016.sampleInfo[process]

if (section == "HiggsPhysics"):
    import HiggsPhysics2016
    samples = HiggsPhysics2016.sampleInfo[process]

count = 0
for sample in samples:
    # fileLists/2016/StandardModelPhysics/Drell-Yan
    sample_name = sample.split("/")[1]
    os.system("dasgoclient -query=\"file dataset={}\" > fileLists/{}/{}/{}/{}.txt".format(sample, year, section, process, sample_name))
    #print("done")
    count+=1
    if (count%10==0): print("Created {} lists.".format(count))

print("{} file lists created for {} {}.".format(count, section, process))
print("Now appending prefix...")

files = os.listdir("fileLists/{}/{}/{}/".format(year, section, process))
for ftxt in files:
    os.system("sed -i -e 's#^#{}#' fileLists/{}/{}/{}/{}".format(prefix, year, section, process, ftxt))
    #print("sed -i -e 's#^#{}#' {}".format(prefix, ftxt))
    #exit()

print("Appended prefix to all files.")
