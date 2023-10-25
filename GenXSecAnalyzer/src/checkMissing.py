import os, sys
import StandardModelPhysics

process = sys.argv[1]
dataset = StandardModelPhysics.sampleInfo[process]

for recid in dataset:
    dname = dataset[recid].split('/')[1]
    fname = '/eos/user/s/sxiaohe/OpenData/MC2015/StandardModelPhysics/{}/{}_{}.json'.format(process, dname, recid)
    if os.path.isfile(fname):
        pass
    else:
        print(recid)
