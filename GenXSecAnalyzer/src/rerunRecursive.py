# cd ..
# python rerunRecursive.py StandardModelPhysics Drell-Yan

import os, sys

section = sys.argv[1]
process = sys.argv[2]
skipexisting = False

if (section == "StandardModelPhysics"):
    import StandardModelPhysics
    samples = StandardModelPhysics.sampleInfo[process]

if (section == "HiggsPhysics"):
    import HiggsPhysics
    samples = HiggsPhysics.sampleInfo[process]

for recid in samples:
    dname = samples[recid].split('/')[1]
    fname = '/eos/user/s/sxiaohe/OpenData/MC2015/{}/{}/{}_{}.json'.format(section, process, dname, recid)
    if os.path.isfile(fname):
        pass
    else:
        cmd = "./src/calculateXSectionAndFilterEfficiency.sh -f recid_{}.txt -s {} -p {} -n 10000000 -k {}".format(recid, section, process, skipexisting)
        print(cmd)
        os.system(cmd)
