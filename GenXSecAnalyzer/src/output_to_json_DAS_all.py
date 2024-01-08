# python src/output_to_json_DAS_all.py 2016 StandardModelPhysics Drell-Yan

import os, sys
import json

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]

fields = ['total_value', 'total_value_uncertainty', 'matching_efficiency', 'filter_efficiency', 'neg_weight_fraction']

directory = 'logs/{}/{}/{}/'.format(year, section, process)
for fname in os.listdir(directory):
    fpath = os.path.join(directory, fname)

    print("Processing log file: ", fpath)
    
    dname = fname.split('xsec_')[-1].split('.')[0]
    metadata = [{"metadata":{"Dataset":dname,
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
    
    with open(fpath) as f:
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

            outfile = '/eos/user/s/sxiaohe/OpenData/MC{}/{}/{}/{}.json'.format(year, section, process, dname)
            with open(outfile, 'w') as jsonfile:
                json.dump(metadata, jsonfile)
                print("Saved to {}".format(outfile))
        except:
            print("Failed saving {} to json.".format(fpath))

