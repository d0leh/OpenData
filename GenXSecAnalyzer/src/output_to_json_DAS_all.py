# python src/output_to_json_DAS_all.py 2016 StandardModelPhysics Drell-Yan

import os, sys
import json
#import StandardModelPhysics2016
import HiggsPhysics2016

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]

directory = 'logs/{}/{}/{}/'.format(year, section, process)
for fname in os.listdir(directory):
    fpath = os.path.join(directory, fname)
    print("Processing log file: {}".format(fpath))
    
    dname = fname.split('xsec_')[-1].split('.')[0]
    with open('fileLists/{}/{}/{}/{}.txt'.format(year, section, process, dname)) as tfile:
        dataset = tfile.readline()[:-1]

    metadata = [{"metadata":{"Dataset":"Name (and location) of the dataset",
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
                             "HepMC_filter_efficiency" : "HepMC filter efficiency (taking into account weights)",
                             "HepMC_filter_efficiency_uncertainty" : "(+-) Error of HepMC filter efficiency (taking into account weights)",
                             "HepMC_filter_efficiency_evt" : "HepMC filter efficiency (event-level)",
                             "HepMC_filter_efficiency_evt_uncertainty" : "(+-) Error of HepMC filter efficiency (event-level)",
                             "filter_efficiency" : "Filter efficiency (taking into account weights)", # to display
                             "filter_efficiency_uncertainty" : "(+-) Error of filter efficiency (taking into account weights)",
                             "filter_efficiency_evt" : "Filter efficiency (event-level)",
                             "filter_efficiency_evt_uncertainty" : "(+-) Error of filter efficiency (event-level)",
                             "neg_weight_fraction":"Final fraction of events with negative weights after filter", # to display
                             "neg_weight_fraction_uncertainty" : "(+-) Error of final fraction of events with negative weights after filter",
                             "equivalent_lumi" : "Final equivalent lumi for 1M events (1/fb)",
                             "equivalent_lumi_uncertainty" : "(+-) Error of final equivalent lumi for 1M events (1/fb)",}}]

    data = {"Dataset":dataset,
            "xsec_before_matching"                    : "-9",
            "xsec_before_matching_uncertainty"        : "-9",
            "xsec_after_matching"                     : "-9", 
            "xsec_after_matching_uncertainty"         : "-9",
            "xsec_before_filter"                      : "-9",
            "xsec_before_filter_uncertainty"          : "-9",
            'total_value'                             : "-9",
            'total_value_uncertainty'                 : "-9",
            'matching_efficiency'                     : "-9",
            "matching_efficiency_uncertainty"         : "-9",
            "HepMC_filter_efficiency"                 : "-9",
            "HepMC_filter_efficiency_uncertainty"     : "-9",
            "HepMC_filter_efficiency_evt"             : "-9",
            "HepMC_filter_efficiency_evt_uncertainty" : "-9",
            'filter_efficiency'                       : "-9",
            "filter_efficiency_uncertainty"           : "-9",
            "filter_efficiency_evt"                   : "-9",
            "filter_efficiency_evt_uncertainty"       : "-9",
            'neg_weight_fraction'                     : "-9",
            "neg_weight_fraction_uncertainty"         : "-9", 
            "equivalent_lumi"                         : "-9", 
            "equivalent_lumi_uncertainty"             : "-9", 
        }

    default = -18
    with open(fpath, 'r') as f:
        contents = f.read().split("\n")    
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
                elif "HepMC filter efficiency (taking into account weights)" in c:
                    data['HepMC_filter_efficiency']             = c.split("= ")[-1].split()[0]
                    data['HepMC_filter_efficiency_uncertainty'] = c.split("= ")[-1].split()[2]
                elif "HepMC filter efficiency (event-level)" in c:
                    data['HepMC_filter_efficiency_evt']             = c.split("= ")[-1].split()[0]
                    data['HepMC_filter_efficiency_evt_uncertainty'] = c.split("= ")[-1].split()[2]

            if(default==-18): # all missing
                print("Unexpected output in log file. Failed saving {} to json".format(fpath))
            else:
                metadata.append(data)
                outfile = '/eos/user/s/sxiaohe/OpenData/MC{}/{}/{}/{}.json'.format(year, section, process, dname)
                with open(outfile, 'w') as jsonfile:
                    json.dump(metadata, jsonfile)
                print("Saved to {}".format(outfile))
        except:
            print("Failed saving {} to json due to unexpected error.".format(fpath))
