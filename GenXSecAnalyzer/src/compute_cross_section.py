# EXAMPLE ON HOW TO RUN
# python ./compute_cross_section.py -f datasets.txt -d process

from optparse import OptionParser
import os
import sys
import commands
import re
import datetime
from time import sleep

def str_to_bool(s):
    if s == 'True':
         return True
    elif s == 'False':
         return False

if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option('-f', '--file'   , dest="inputFilelist", default='',       help='input text file of root files')
    parser.add_option('-s', '--section', dest="sectionName"  , default='',       help='section on Open Data Portal')
    parser.add_option('-p', '--process', dest="processName"  , default='',       help='name of the dataset')
    parser.add_option('-n', '--events' , dest="events"       , default=int(1e7), help='number of events to calculate the cross section')
    parser.add_option('-k', '--skipexisting', dest="skipexisting",  default=False,    help='skipexisting existing output files containing xsec results')

    (args, opts) = parser.parse_args(sys.argv)

    inputFilelist = "fileLists/{}/{}/{}".format(args.sectionName, args.processName, args.inputFilelist)
    recid = args.inputFilelist.split('_')[1].split('.')[0]
    outfileName = "logs/{}/{}/xsec_{}.log".format(args.sectionName, args.processName, recid)
    skipexisting = str_to_bool(str(args.skipexisting))

    if skipexisting and os.path.isfile(outfileName): 
        print "{} existing and NO skipexisting asked, skipping".format(outfileName)
    else:
        filelist = open(inputFilelist, 'r').read().split('\n')
        inputFiles = ""
        for rootfile in filelist:
            if('root' in rootfile):
                inputFiles += ' inputFiles='+rootfile + ' '
   
        # compute cross section
        command = 'cmsRun src/genXSecAnalyzer_cfg.py {} maxEvents={} 2>&1 | tee {}'.format(inputFiles, str(args.events), outfileName)
        print command
