# cd ..
# python rerunRecursive.py StandardModelPhysics Drell-Yan

import os, sys

section = sys.argv[1]
process = sys.argv[2]
skipexisting = False

if (section == "StandardModelPhysics"):
    import StandardModelPhysics
    samples = {"Drell-Yan"  :StandardModelPhysics.sampleInfo["Drell-Yan"],
           "ElectroWeak":StandardModelPhysics.sampleInfo["ElectroWeak"],
           "MinimumBias":StandardModelPhysics.sampleInfo["MinimumBias"],
           "QCD"        :StandardModelPhysics.sampleInfo["QCD"],
           "TopPhysics" :StandardModelPhysics.sampleInfo["TopPhysics"],
       }

if (section == "HiggsPhysics"):
    import HiggsPhysics
    samples = {#"BeyondStandardModel": HiggsPhysics.sampleInfo["BeyondStandardModel"],
               "StandardModel": HiggsPhysics.sampleInfo["StandardModel"],
    }

dataset = StandardModelPhysics.sampleInfo[process]

for recid in dataset:
    dname = dataset[recid].split('/')[1]
    fname = '/eos/user/s/sxiaohe/OpenData/MC2015/{}/{}/{}_{}.json'.format(section, process, dname, recid)
    if os.path.isfile(fname):
        pass
    else:
        cmd = "./src/calculateXSectionAndFilterEfficiency.sh -f recid_{}.txt -s {} -p {} -n 10000000".format(recid, section, process)
        print(cmd)
        os.system(cmd)
