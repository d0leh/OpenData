#python3 src/flag_rootfiles.py 2016 StandardModelPhysics ElectroWeak

import os, sys
import json
import StandardModelPhysics2016

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]

directory = 'logs/{}/{}/{}/'.format(year, section, process)

print("Checking failed files...")
outdir = 'flagged/{}/{}/{}/{}/'.format('fail', year, section, process)
if not os.path.exists(outdir):
    os.makedirs(outdir)
for fname in os.listdir(directory):
    dname = fname.split('xsec_')[-1].split('.')[0]
    fpath = os.path.join(directory, fname)

    list_fail = []
    with open(fpath, 'r') as f:
        contents = f.read().split("\n")
        for c in contents:
            if "Failed to open file at URL" in c:
                root_fail = c.split('Failed to open file at URL ')[1].split('?tried')[0]
                list_fail.append(root_fail+'\n')
                print("Found failed file: {}".format(root_fail))
    if(len(list_fail)>0):
        ofile = open('{}{}.txt'.format(outdir, dname), 'w+')
        ofile.writelines(list_fail)
        print("Writing failed files to {}".format('{}{}.txt'.format(outdir, dname)))


print("Checking duplicate events...")
outdir = 'flagged/{}/{}/{}/{}/'.format('duplicate', year, section, process)
if not os.path.exists(outdir):
    os.makedirs(outdir)
for fname in os.listdir(directory):
    dname = fname.split('xsec_')[-1].split('.')[0]
    fpath = os.path.join(directory, fname)

    list_duplicate = []
    with open(fpath, 'r') as f:
        contents = f.read().split("\n")
        for c in contents:
            if "The duplicate was from file " in c:
                root_duplicate = c.split("The duplicate was from file ")[1][:-1]
                if root_duplicate+'\n' not in list_duplicate:
                    list_duplicate.append(root_duplicate+'\n')
                    print("Found duplicated events in file: {}".format(root_duplicate))
    if(len(list_duplicate)>0):
        ofile = open('{}{}.txt'.format(outdir, dname), 'w+')
        ofile.writelines(list_duplicate)
        print("Writing files with duplicated events to {}".format('{}{}.txt'.format(outdir, dname)))
