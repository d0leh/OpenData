# cd ..
# python src/makeFileLists_DAS.py 2016 StandardModelPhysics Drell-Yan False False False

# Two debug handles. First one set to True to check which files are missing. Second one set to True to check duplicate sample names.
# dasgoclient -query="file dataset=/DY1JetsToLL_M-10to50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM"

# The last argument: set to True to keep extensions as separate files; set to False to combine them into one single file

import os, sys

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]
check_missing = sys.argv[4]
check_duplicates = sys.argv[5]
separate = sys.argv[6]

prefix = "root://cmsxrootd.fnal.gov/"

if (section == "StandardModelPhysics"):
    import StandardModelPhysics2017
    samples = StandardModelPhysics2017.sampleInfo[process]

if (section == "HiggsPhysics"):
    import HiggsPhysics2017
    samples = HiggsPhysics2017.sampleInfo[process]

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
    newfile = True

    if('{}.txt'.format(sample_name) in files):
        # Create separate .txt files for extensions
        if(separate=="True"):
            if('{}.txt'.format(sample_name+'_2') in files):
                sample_name = sample_name+'_3'
                print(sample_name)
            elif('{}.txt'.format(sample_name+'_1') in files):
                sample_name = sample_name+'_2'
                print(sample_name)
            else:
                sample_name = sample_name+'_1'
                print(sample_name)
        else:
            newfile = False
    
    if("RunIISummer20UL16MiniAODv2-106X" in sample_name):
        print(sample)
        exit()

    outfile = "fileLists/{}/{}/{}/{}.txt".format(year, section, process, sample_name)
    if(newfile):
        with open(outfile, "w") as f:
            f.write(sample+'\n')
    os.system("dasgoclient -query=\"file dataset={}\" >> {}".format(sample, outfile))
    count+=1
    if (count%10==0): print("Created {} lists.".format(count))

print("{} file lists created for {} {}.".format(count, section, process))
print("Now appending prefix...")

files = os.listdir("fileLists/{}/{}/{}/".format(year, section, process))
for ftxt in files:
    os.system("sed -i -e '1 ! s#^#{}#' fileLists/{}/{}/{}/{}".format(prefix, year, section, process, ftxt))

print("Appended prefix to all files.")
