# cd ..
# python src/makeFileLists_DAS.py 2016 StandardModelPhysics Drell-Yan True

# dasgoclient -query="file dataset=/DY1JetsToLL_M-10to50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM"

import os, sys

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]
check_missing = sys.argv[4]
check_duplicates = sys.argv[5]

prefix = "root://cmsxrootd.fnal.gov/"

if (section == "StandardModelPhysics"):
    import StandardModelPhysics2016
    samples = StandardModelPhysics2016.sampleInfo[process]

if (section == "HiggsPhysics"):
    import HiggsPhysics2016
    samples = HiggsPhysics2016.sampleInfo[process]

if(check_missing=="True"):
    count = 0
    files = os.listdir("fileLists/{}/{}/{}/".format(year, section, process))
    print(len(files))
    for sample in samples:
        sample_name = sample.split("/")[1]
        if '{}.txt'.format(sample_name) in files:
            pass
        else:
            count+=1
            print('{}.txt does not exist'.format(sample))
    print('Missing {} files.'.format(count))
    exit()

if(check_duplicates=="True"):
    count = 0
    files = os.listdir("fileLists/{}/{}/{}/".format(year, section, process))
    for sample in samples:
        #print(sample == samples)
        if (sum(sample==samples))!=1:
            print(sample==samples)
        #exit()
    exit()

count = 0
for sample in samples:
    # fileLists/2016/StandardModelPhysics/Drell-Yan
    sample_name = sample.split("/")[1]
    files = os.listdir("fileLists/{}/{}/{}/".format(year, section, process))
    triggered = False
    if('{}.txt'.format(sample_name+'_2') in files):
        sample_name = sample_name+'_3'
        triggered = True
    elif('{}.txt'.format(sample_name+'_1') in files):
        sample_name = sample_name+'_2'
        triggered = True
    elif('{}.txt'.format(sample_name) in files):
        sample_name = sample_name+'_1'
        triggered = True
    if(triggered):
        print(sample_name)
    
    os.system("dasgoclient -query=\"file dataset={}\" > fileLists/{}/{}/{}/{}.txt".format(sample, year, section, process, sample_name))
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
