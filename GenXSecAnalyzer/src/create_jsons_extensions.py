# python create_jsons_extensions.py 2016 StandardModelPhysics Drell-Yan

# copies the original json into json files for extensions

import os, sys

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]

import StandardModelPhysics2016
samples = StandardModelPhysics2016.sampleInfo[process]

for sample in samples:
    if("ext" in sample):
        print("Found an extension: {}".format(sample))
        sample_name = sample.split("/")[1]

        if('{}.txt'.format(sample_name+'_2') in files):
            dname = sample_name+'_3'
        elif('{}.txt'.format(sample_name+'_1') in files):
            dname = sample_name+'_2'
        else:
            dname = sample_name+'_1'

        infile = '/eos/user/s/sxiaohe/OpenData/MC{}/{}/{}/{}.json'.format(year, section, process, sample_name)
        outfile = '/eos/user/s/sxiaohe/OpenData/MC{}/{}/{}/{}.json'.format(year, section, process, dname)

        print("Creating json file: {}".format(outfile))
        os.system("cp {} {}".format(infile, outfile))
        
        
