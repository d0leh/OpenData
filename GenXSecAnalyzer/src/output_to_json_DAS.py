# python output_to_json.py recid_.txt 2016 StandardModelPhysics Drell-Yan

import os, sys
import json
#import StandardModelPhysics2016

label   = sys.argv[1]
year    = sys.argv[2]
section = sys.argv[3]
process = sys.argv[4]

#dname = dataset.split('/')[1]
fname = 'logs/{}/{}/{}/xsec_{}.log'.format(year, section, process, label)
print("Processing log file: ", fname)

fields = ['total_value', 'total_value_uncertainty', 'matching_efficiency', 'filter_efficiency', 'neg_weight_fraction']

metadata = [{"metadata":{"Dataset":dataset,
                         "total_value":"Total cross section after matching/filter (pb)",
                         "total_value_uncertainty":"(+-) Error of total cross section (pb)",
                         "matching_efficiency":"Matching efficiency",
                         "filter_efficiency":"Filter efficiency (taking into account weights)",
                         "neg_weight_fraction":"Final fraction of events with negative weights after filter",}}]

data = {'total_value':-1,
        'total_value_uncertainty':-1,
        'matching_efficiency':-1,
        'matching_efficiency':-1,
        'neg_weight_fraction':-1,
}

with open(fname) as f:
    contents = f.read().split("\n")

    ###### CAVEAT: for some versions of CMSSW, the output descriptions might have typos such as "filtre"
    ###### Assume no typo for now, check later
    try:
        data['total_value'] = ([c for c in contents if "After filter: final cross section" in c][0].split("= ")[-1].split())[0] # val
        data['total_value_uncertainty'] = ([c for c in contents if "After filter: final cross section" in c][0].split("= ")[-1].split())[2] # err
        data['matching_efficiency'] = ([c for c in contents if "Matching efficiency" in c][0].split("= ")[-1].split())[0]
        data['filter_efficiency'] = ([c for c in contents if "Filter efficiency (taking into account weights)" in c][0].split("= ")[-1].split())[0]
        data['neg_weight_fraction'] = ([c for c in contents if "After filter: final fraction of events with negative weights" in c][0].split("= ")[-1].split())[0]

        metadata.append(data)
        
    except:
        print("Failed saving {} to json.".format(fname))

outfile = '/eos/user/s/sxiaohe/OpenData/MC{}/{}/{}/{}_{}.json'.format(year, section, process, dname, recid)
with open(outfile, 'w') as jsonfile:
    json.dump(metadata, jsonfile)
    print("Saved to {}".format(outfile))
