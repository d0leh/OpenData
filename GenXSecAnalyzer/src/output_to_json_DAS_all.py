# python src/output_to_json_DAS_all.py 2016 StandardModelPhysics Drell-Yan

import os, sys
import json

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]

fields = ['xsec_before_matching', 'xsec_before_matching_uncertainty', 
          'xsec_after_matching', 'xsec_after_matching_uncertainty', 
          'xsec_before_filter', 'xsec_before_filter_uncertainty',
          'total_value', 'total_value_uncertainty', # final xsec value
          'matching_efficiency', 'matching_efficiency_uncertainty', 
          'filter_efficiency', 'filter_efficiency_uncertainty', # taking into account weights
          'filter_efficiency_evt', 'filter_efficiency_evt_uncertainty', # event level
          'neg_weight_fraction', 'neg_weight_fraction_uncertainty', 
          'equivalent_lumi', 'equivalent_lumi_uncertainty']

metadata = [{"metadata":{#"Dataset":"",
                         "xsec_before_matching" : "Total cross section before matching (pb)",
                         "xsec_before_matching_uncertainty": "(+-) Error of total cross section before matching (pb)",
                         "xsec_after_matching": "Total cross section after matching (pb)",
                         "xsec_after_matching_uncertainty": "(+-) Error of total cross section after matching (pb)",
                         "xsec_before_filter" : "Total cross section before filter (pb)",
                         "xsec_before_filter_uncertainty" : "(+-) Error of total cross section before filter (pb)",
                         "total_value" : "Final total cross section (pb)", # to display
                         "total_value_uncertainty" : "(+-) Error of final total cross section (pb)", # to display
                         "matching_efficiency" : "Matching efficiency",
                         "matching_efficiency_uncertainty" : "(+-) Error of matching efficiency",
                         "filter_efficiency" : "Filter efficiency (taking into account weights)", # to display
                         "filter_efficiency_uncertainty" : "(+-) Error of filter efficiency (taking into account weights)",
                         "filter_efficiency_evt" : "Filter efficiency (event-level)",
                         "filter_efficiency_evt_uncertainty" : "(+-) Error of filter efficiency (event-level)",
                         "neg_weight_fraction":"Final fraction of events with negative weights after filter", # to display
                         "neg_weight_fraction_uncertainty" : "(+-) Error of final fraction of events with negative weights after filter",
                         "equivalent_lumi" : "Final equivalent lumi for 1M events (1/fb)",
                         "equivalent_lumi_uncertainty" : "(+-) Error of final equivalent lumi for 1M events (1/fb)",}}]

directory = 'logs/{}/{}/{}/'.format(year, section, process)
for fname in os.listdir(directory):
    fpath = os.path.join(directory, fname)

    print("Processing log file: ", fpath)
    
    dname = fname.split('xsec_')[-1].split('.')[0]
    print(dname)

    data = {"xsec_before_matching"              : -1,
            "xsec_before_matching_uncertainty"  : -1,
            "xsec_after_matching"               : -1, 
            "xsec_after_matching_uncertainty"   : -1,
            "xsec_before_filter"                : -1,
            "xsec_before_filter_uncertainty"    : -1,
            'total_value'                       : -1,
            'total_value_uncertainty'           : -1,
            'matching_efficiency'               : -1,
            "matching_efficiency_uncertainty"   : -1,
            'filter_efficiency'                 : -1,
            "filter_efficiency_uncertainty"     : -1,
            "filter_efficiency_evt"             : -1,
            "filter_efficiency_evt_uncertainty" : -1,
            'neg_weight_fraction'               : -1,
            "neg_weight_fraction_uncertainty"   : -1, 
            "equivalent_lumi"                   : -1, 
            "equivalent_lumi_uncertainty"       : -1, 
        }

    with open(fpath) as f:
        contents = f.read().split("\n")    
        default = -18
        ###### CAVEAT: for some versions of CMSSW, the output descriptions might have typos such as "filtre"
        ###### Assume no typo for now, check later
        try:
            for c in contents:
                if "Before matching: total cross section" in c:
                    data['xsec_before_matching']             = c.split("= ")[-1].split()[0]
                    data['xsec_before_matching_uncertainty'] = c.split("= ")[-1].split()[2]
                    default+=1
                elif "After matching: total cross section" in c:
                    data['xsec_after_matching']             = c.split("= ")[-1].split()[0]
                    data['xsec_after_matching_uncertainty'] = c.split("= ")[-1].split()[2]
                    default+=1
                elif "Before Filtrer: total cross section" in c: # take into account a possible typo
                    data['xsec_before_filter']             = c.split("= ")[-1].split()[0]
                    data['xsec_before_filter_uncertainty'] = c.split("= ")[-1].split()[2]
                    default+=1
                elif "Before Filter: total cross section" in c: 
                    data['xsec_before_filter']             = c.split("= ")[-1].split()[0]
                    data['xsec_before_filter_uncertainty'] = c.split("= ")[-1].split()[2]
                    default+=1
                elif "After filter: final cross section" in c:
                    data['total_value']             = c.split("= ")[-1].split()[0] # val
                    data['total_value_uncertainty'] = c.split("= ")[-1].split()[2] # err
                    default+=1
                elif "Matching efficiency" in c:
                    data['matching_efficiency']             = c.split("= ")[-1].split()[0]
                    data['matching_efficiency_uncertainty'] = c.split("= ")[-1].split()[2]
                    default+=1
                elif "Filter efficiency (taking into account weights)" in c:
                    data['filter_efficiency']             = c.split("= ")[-1].split()[0]
                    data['filter_efficiency_uncertainty'] = c.split("= ")[-1].split()[2]
                    default+=1
                elif "Filter efficiency (event-level)" in c:
                    data['filter_efficiency_evt']             = c.split("= ")[-1].split()[0]
                    data['filter_efficiency_evt_uncertainty'] = c.split("= ")[-1].split()[2]
                    default+=1
                elif "After filter: final fraction of events with negative weights" in c:
                    data['neg_weight_fraction']             = c.split("= ")[-1].split()[0]
                    data['neg_weight_fraction_uncertainty'] = c.split("= ")[-1].split()[2]
                    default+=1
                elif "final equivalent lumi for 1M events (1/fb)" in c:
                    data['equivalent_lumi']             = c.split("= ")[-1].split()[0]
                    data['equivalent_lumi_uncertainty'] = c.split("= ")[-1].split()[2]
                    default+=1

            if(default==-18):
                print("Unexpected output in log file. Failed saving {} to json".format(fpath))
            else:
                metadata.append(data)
                outfile = '/eos/user/s/sxiaohe/OpenData/MC{}/{}/{}/{}.json'.format(year, section, process, dname)
                with open(outfile, 'w') as jsonfile:
                    json.dump(metadata, jsonfile)
                print("Saved to {}".format(outfile))
        except:
            print("Failed saving {} to json due to unexpected error.".format(fpath))

