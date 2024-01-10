# cd ..
# python src/rerunRecursive_DAS.py 2016 StandardModelPhysics Drell-Yan False
# if count = True, counts the number of missing jsons
# if count = False, reruns the missing jobs

import os, sys
import StandardModelPhysics2016

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]
count   = sys.argv[4]
skipexisting = False

#directory = "fileLists/{}/{}/{}/".format(year, section, process)
files = os.listdir("fileLists/{}/{}/{}/".format(year, section, process))

if (count=="True"):
    N_missing = 0
    for txtfile in files:
        dname = txtfile.split('.')[0]
        if os.path.isfile('/eos/user/s/sxiaohe/OpenData/MC{}/{}/{}/{}.json'.format(year, section, process, dname)):
            pass
        else:
            print("Missing {}.json".format(dname))
            N_missing+=1
    print("Missing {} files.".format(N_missing))
else:
    for txtfile in files:
        dname = txtfile.split('.')[0]
        if os.path.isfile('/eos/user/s/sxiaohe/OpenData/MC{}/{}/{}/{}.json'.format(year, section, process, dname)):
            pass
        else:
            cmd = "./src/calculateXSectionAndFilterEfficiency.sh -f {} -y {} -s {} -p {} -n 10000000 -k {}".format(dname, year, section, process, skipexisting)
            print(cmd)
            os.system(cmd)
