# cd ..
# python src/runRecursive_DAS.py 2016 StandardModelPhysics Drell-Yan

import os, sys
#import StandardModelPhysics2016
import HiggsPhysics2016

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]
skipexisting = False

count = 0
#directory = "fileLists/{}/{}/{}/".format(year, section, process)
files = os.listdir("fileLists/{}/{}/{}/".format(year, section, process))

for txtfile in files:
    txtfile = txtfile.split('.')[0]
    cmd = "./src/calculateXSectionAndFilterEfficiency.sh -f {} -y {} -s {} -p {} -n 10000000 -k {}".format(txtfile, year, section, process, skipexisting)
    print(cmd)
    os.system(cmd)
    count+=1
    print("Processed {} samples.".format(count))
    
print("Finished running all the samples.")    
