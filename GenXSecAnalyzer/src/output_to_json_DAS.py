# python output_to_json_DAS.py 2016 StandardModelPhysics Drell-Yan filename

import os, sys
import json
#import StandardModelPhysics2016

year    = sys.argv[1]
section = sys.argv[2]
process = sys.argv[3]
fname   = sys.argv[4]

print("Processing log file: ", fname)
dname = fname.split('xsec_')[-1].split('.')[0]

fields = ['xsec_before_matching', 'xsec_before_matching_uncertainty', 
          'xsec_after_matching', 'xsec_after_matching_uncertainty', 
          'xsec_before_filter', 'xsec_before_filter_uncertainty',
          'total_value', 'total_value_uncertainty', # final xsec value
          'matching_efficiency', 'matching_efficiency_uncertainty', 
          'filter_efficiency', 'filter_efficiency_uncertainty', # taking into account weights
          'filter_efficiency_evt', 'filter_efficiency_evt_uncertainty', # event level
          'neg_weight_fraction', 'neg_weight_fraction_uncertainty', 
          'equivalent_lumi', 'equivalent_lumi_uncertainty']

metadata = [{"metadata":{"Dataset":dname,
                         "xsec_before_matching" : "Total cross section before matching (pb)",
                         "xsec_before_matching_uncertainty": "(+-) Error of total cross section before matching (pb)",
                         "xsec_after_matching": "Total cross section after matching (pb)",
                         "xsec_after_matching_uncertainty": "(+-) Error of total cross section after matching (pb)",
                         "xsec_before_filter" : "Total cross section before filter (pb)",
                         "xsec_before_filter_uncertainty" : "(+-) Error of total cross section before filter (pb)",
                         "total_value" : "Total cross section after matching/filter (pb)", # to display
                         "total_value_uncertainty" : "(+-) Error of total cross section (pb)", # to display
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

with open('logs/{}/{}/{}/{}'.format(year, section, process, fname)) as f:
    contents = f.read().split("\n")

    ###### CAVEAT: for some versions of CMSSW, the output descriptions might have typos such as "filtre"
    ###### Assume no typo for now, check later
    try:
        xsec_before_matching  = [c for c in contents if "Before matching: total cross section" in c][0].split("= ")[-1].split()
        xsec_after_matching   = [c for c in contents if "After matching: total cross section" in c][0].split("= ")[-1].split()
        xsec_before_filter    = [c for c in contents if "Before Filtrer: total cross section" in c][0].split("= ")[-1].split() # take into account a possible typo
        xsec_before_filter    = [c for c in contents if "Before Filter: total cross section" in c][0].split("= ")[-1].split()
        total_value           = [c for c in contents if "After filter: final cross section" in c][0].split("= ")[-1].split()
        matching_efficiency   = [c for c in contents if "Matching efficiency" in c][0].split("= ")[-1].split()
        filter_efficiency     = [c for c in contents if "Filter efficiency (taking into account weights)" in c][0].split("= ")[-1].split()
        filter_efficiency_evt = [c for c in contents if "Filter efficiency (event-level)" in c][0].split("= ")[-1].split()
        neg_weight_fraction   = [c for c in contents if "After filter: final fraction of events with negative weights" in c][0].split("= ")[-1].split()
        equivalent_lumi       = [c for c in contents if "final equivalent lumi for 1M events (1/fb)" in c][0].split("= ")[-1].split()

        data['xsec_before_matching']              = xsec_before_matching[0]
        data['xsec_before_matching_uncertainty']  = xsec_before_matching[2]
        data['xsec_after_matching']               = xsec_after_matching[0]
        data['xsec_after_matching_uncertainty']   = xsec_after_matching[2]
        data['xsec_before_filter']                = xsec_before_filter[0]
        data['xsec_before_filter_uncertainty']    = xsec_before_filter[2]
        data['total_value']                       = total_value[0] # val
        data['total_value_uncertainty']           = total_value[2] # err
        data['matching_efficiency']               = matching_efficiency[0]
        data['matching_efficiency_uncertainty']   = matching_efficiency[2]
        data['filter_efficiency']                 = filter_efficiency[0]
        data['filter_efficiency_uncertainty']     = filter_efficiency[2]
        data['filter_efficiency_evt']             = filter_efficiency_evt[0]
        data['filter_efficiency_evt_uncertainty'] = filter_efficiency_evt[2]
        data['neg_weight_fraction']               = neg_weight_fraction[0]
        data['neg_weight_fraction_uncertainty']   = neg_weight_fraction[2]
        data['equivalent_lumi']                   = equivalent_lumi[0]
        data['equivalent_lumi_uncertainty']       = equivalent_lumi[2]
        metadata.append(data)
    except:
        print("Failed saving {} to json.".format(fname))

outfile = '/eos/user/s/sxiaohe/OpenData/MC{}/{}/{}/{}.json'.format(year, section, process, dname)
with open(outfile, 'w') as jsonfile:
    json.dump(metadata, jsonfile)
    print("Saved to {}".format(outfile))
