import os, sys
import json
import StandardModelPhysics

recid = sys.argv[1].split('_')[1].split('.')[0]
process = sys.argv[2]
dataset = StandardModelPhysics.sampleInfo[process][recid]
dname = dataset.split('/')[1]
fname = 'logs/xsec_{}.log'.format(recid)
print("Processing log file: ", fname)

try:
    fields = ['totX_beforeMat', 'totX_beforeMat_err', 'totX_afterMat', 'totX_afterMat_err', 'matchingEff', 'matchingEff_err', 'filterEff_weights', 'filterEff_weights_err', 'filterEff_event', 'filterEff_event_err', 'totX_final', 'totX_final_err', 'negWeightFrac', 'negWeightFrac_err', 'equivLumi', 'equivLumi_err']

    metadata = [{"metadata":{"Dataset":dataset,
                             "totX_beforeMat":"Total cross section before matching (pb)",
                             "totX_beforeMat_err":"(+-) Error of total cross section before matching (pb)",
                             "totX_afterMat":"Total cross section after matching (pb)",
                             "totX_afterMat_err":"(+-) Error of total cross section after matching (pb)",
                             "matchingEff":"Matching efficiency",
                             "matchingEff_err":"(+-) Error of matching efficiency",
                             "filterEff_weights":"Filter efficiency (taking into account weights)",
                             "filterEff_weights_err":"(+-) Error of filter efficiency (taking into account weights)",
                             "filterEff_event":"Filter efficiency (event-level)",
                             "filterEff_event_err":"(+-) Error of filter efficiency (event-level)",
                             "totX_final":"Final cross senction after filter (pb)",
                             "totX_final_err":"(+-) Error of final cross section after filter (pb)",
                             "negWeightFrac":"Final fraction of events with negative weights after filter",
                             "negWeightFrac_err":"(+-) Error of final fraction of events with negative weights after filter",
                             "equivLumi":"Final equivalent lumi for 1M events (1/fb)",
                             "equivLumi_err":"(+-) Error of final equivalent lumi for 1M events (1/fb)", }}]

    with open(fname) as f:
        contents = f.read().split("\n")
        
        totX_beforeMat = [c for c in contents if "Before matching: total cross section" in c][0].split("= ")[-1].split() # val and err
        totX_afterMat = [c for c in contents if "After matching: total cross section" in c][0].split("= ")[-1].split()
        matchingEff = [c for c in contents if "Matching efficiency" in c][0].split("= ")[-1].split()
        filterEffWeights = [c for c in contents if "Filter efficiency (taking into account weights)" in c][0].split("= ")[-1].split()
        filterEffEvent = [c for c in contents if "Filter efficiency (event-level)" in c][0].split("= ")[-1].split()
        totX_final = [c for c in contents if "After filter: final cross section" in c][0].split("= ")[-1].split()
        negWeightFrac = [c for c in contents if "After filter: final fraction of events with negative weights" in c][0].split("= ")[-1].split()
        equivLumi = [c for c in contents if "final equivalent lumi for 1M events (1/fb)" in c][0].split("= ")[-1].split()
            
        rows = ['0.0']*16
    
        rows[0] = totX_beforeMat[0]
        rows[1] = totX_beforeMat[2]
    
        rows[2] = totX_afterMat[0]
        rows[3] = totX_afterMat[2]
    
        rows[4] = matchingEff[0]
        rows[5] = matchingEff[2]
    
        rows[6] = filterEffWeights[0]
        rows[7] = filterEffWeights[2]
    
        rows[8] = filterEffEvent[0]
        rows[9] = filterEffEvent[2]
    
        rows[10] = totX_final[0]
        rows[11] = totX_final[2]
        
        rows[12] = negWeightFrac[0]
        rows[13] = negWeightFrac[2]
    
        rows[14] = equivLumi[0]
        rows[15] = equivLumi[2]
    
        data = dict(zip(fields, rows))
        metadata.append(data)
    
        outfile = '/eos/user/s/sxiaohe/OpenData/MC2015/StandardModelPhysics/{}/{}_{}.json'.format(process, dname, recid)
        with open(outfile, 'w') as jsonfile:
            json.dump(metadata, jsonfile)
            print("Saved to {}".format(outfile))
except:
    print("Failed saving {} in format 1. Trying format 2.".format(fname))

    try: # saw in Drell-Yan (not full sample)
        fields = ['totX_beforeMat', 'totX_beforeMat_err', 'totX_afterMat', 'totX_afterMat_err', 'filterEff_weights', 'filterEff_weights_err', 'filterEff_event', 'filterEff_event_err', 'totX_final', 'totX_final_err']

        metadata = [{"metadata":{"Dataset":dataset,
                                 "totX_beforeMat":"Total cross section before matching (pb)",
                                 "totX_beforeMat_err":"(+-) Error of total cross section before matching (pb)",
                                 "totX_afterMat":"Total cross section after matching (pb)",
                                 "totX_afterMat_err":"(+-) Error of total cross section after matching (pb)",
                                 "filterEff_weights":"Filter efficiency (taking into account weights)",
                                 "filterEff_weights_err":"(+-) Error of filter efficiency (taking into account weights)",
                                 "filterEff_event":"Filter efficiency (event-level)",
                                 "filterEff_event_err":"(+-) Error of filter efficiency (event-level)",
                                 "totX_final":"Final cross senction after filter (pb)",
                                 "totX_final_err":"(+-) Error of final cross section after filter (pb)", }}]
    
        with open(fname) as f:
            contents = f.read().split("\n")

            totX_beforeMat = [c for c in contents if "Before matching: total cross section" in c][0].split("= ")[-1].split()
            totX_afterMat = [c for c in contents if "After matching: total cross section" in c][0].split("= ")[-1].split()
            filterEffWeights = [c for c in contents if "Filter efficiency (taking into account weights)" in c][0].split("= ")[-1].split()
            filterEffEvent = [c for c in contents if "Filter efficiency (event-level)" in c][0].split("= ")[-1].split()
            totX_final = [c for c in contents if "After filter: final cross section" in c][0].split("= ")[-1].split()
            
            rows = ['0.0']*10

            rows[0] = totX_beforeMat[0]
            rows[1] = totX_beforeMat[2]

            rows[2] = totX_afterMat[0]
            rows[3] = totX_afterMat[2]
                        
            rows[4] = filterEffWeights[0]
            rows[5] = filterEffWeights[2]
            
            rows[6] = filterEffEvent[0]
            rows[7] = filterEffEvent[2]
            
            rows[8] = totX_final[0]
            rows[9] = totX_final[2]

            data = dict(zip(fields, rows))
            metadata.append(data)

            outfile = '/eos/user/s/sxiaohe/OpenData/MC2015/StandardModelPhysics/{}/{}_{}.json'.format(process, dname, recid)
            with open(outfile, 'w') as jsonfile:
                json.dump(metadata, jsonfile)
            print("Saved to {}".format(outfile))
    except:
        print("Failed saving {} in format 2. Trying format 3.".format(fname))

        try: # saw in QCD
            fields = ['totX_beforeFilter', 'totX_beforeFilter_err', 'filterEff_weights', 'filterEff_weights_err', 'filterEff_event', 'filterEff_event_err', 'totX_final', 'totX_final_err', 'negWeightFrac', 'negWeightFrac_err', 'equivLumi', 'equivLumi_err']
            metadata = [{"metadata":{"Dataset":dataset,
                                     "totX_beforeFilter":"Total cross section before filter (pb)",
                                     "totX_beforeFilter_err":"(+-) Error of total cross section before filter (pb)",
                                     "filterEff_weights":"Filter efficiency (taking into account weights)",
                                     "filterEff_weights_err":"(+-) Error of filter efficiency (taking into account weights)",
                                     "filterEff_event":"Filter efficiency (event-level)",
                                     "filterEff_event_err":"(+-) Error of filter efficiency (event-level)",
                                     "totX_final":"Final cross senction after filter (pb)",
                                     "totX_final_err":"(+-) Error of final cross section after filter (pb)",
                                     "negWeightFrac":"Final fraction of events with negative weights after filter",
                                     "negWeightFrac_err":"(+-) Error of final fraction of events with negative weights after filter",
                                     "equivLumi":"Final equivalent lumi for 1M events (1/fb)",
                                     "equivLumi_err":"(+-) Error of final equivalent lumi for 1M events (1/fb)", }}]
            
            with open(fname) as f:
                contents = f.read().split("\n")
                
                totX_beforeFilter = [c for c in contents if "Before Filter: total cross section" in c][0].split("= ")[-1].split()
                filterEffWeights = [c for c in contents if "Filter efficiency (taking into account weights)" in c][0].split("= ")[-1].split()
                filterEffEvent = [c for c in contents if "Filter efficiency (event-level)" in c][0].split("= ")[-1].split()
                totX_final = [c for c in contents if "After filter: final cross section" in c][0].split("= ")[-1].split()
                negWeightFrac = [c for c in contents if "After filter: final fraction of events with negative weights" in c][0].split("= ")[-1].split()
                equivLumi = [c for c in contents if "final equivalent lumi for 1M events (1/fb)" in c][0].split("= ")[-1].split()
                
                rows = ['0.0']*12
                
                rows[0] = totX_beforeFilter[0] # value
                rows[1] = totX_beforeFilter[2] # error
                
                rows[2] = filterEffWeights[0]
                rows[3] = filterEffWeights[2]
                
                rows[4] = filterEffEvent[0]
                rows[5] = filterEffEvent[2]
                
                rows[6] = totX_final[0]
                rows[7] = totX_final[2]
                
                rows[8] = negWeightFrac[0]
                rows[9] = negWeightFrac[2]
                
                rows[10] = equivLumi[0]
                rows[11] = equivLumi[2]
                
                data = dict(zip(fields, rows))
                metadata.append(data)

                outfile = '/eos/user/s/sxiaohe/OpenData/MC2015/StandardModelPhysics/{}/{}_{}.json'.format(process, dname, recid)
                with open(outfile, 'w') as jsonfile:
                    json.dump(metadata, jsonfile)
                    print("Saved to {}".format(outfile))
        except:
            print("Failed saving {} in format 3. Trying format 4.".format(fname))
            try: # saw in MinimumBias
                fields = ['totX_beforeFilter', 'totX_beforeFilter_err', 'filterEff(weights)', 'filterEff(weights)_err', 'filterEff(event)', 'filterEff(event)_err', 'totX_final', 'totX_final_err']
                metadata = [{"metadata":{"Dataset":dataset,
                                         "totX_beforeFilter":"Total cross section before filter (pb)",
                                         "totX_beforeFilter_err":"(+-) Error of total cross section before filter (pb)",
                                         "filterEff_weights":"Filter efficiency (taking into account weights)",
                                         "filterEff_weights_err":"(+-) Error of filter efficiency (taking into account weights)",
                                         "filterEff_event":"Filter efficiency (event-level)",
                                         "filterEff_event_err":"(+-) Error of filter efficiency (event-level)",
                                         "totX_final":"Final cross senction after filter (pb)",
                                         "totX_final_err":"(+-) Error of final cross senction after filter (pb)", }}]
                
                with open(fname) as f:
                    contents = f.read().split("\n")
                    
                    totX_beforeFilter = [c for c in contents if "Before Filter: total cross section" in c][0].split("= ")[-1].split() # val and err
                    filterEffWeights = [c for c in contents if "Filter efficiency (taking into account weights)" in c][0].split("= ")[-1].split()
                    filterEffEvent = [c for c in contents if "Filter efficiency (event-level)" in c][0].split("= ")[-1].split()
                    totX_final = [c for c in contents if "After filter: final cross section" in c][0].split("= ")[-1].split()
                    
                    rows = ['0.0']*8
                    
                    rows[0] = totX_beforeFilter[0]
                    rows[1] = totX_beforeFilter[2]
                    
                    rows[2] = filterEffWeights[0]
                    rows[3] = filterEffWeights[2]
                    
                    rows[4] = filterEffEvent[0]
                    rows[5] = filterEffEvent[2]
                    
                    rows[6] = totX_final[0]
                    rows[7] = totX_final[2]
                    
                    data = dict(zip(fields, rows))        
                    metadata.append(data)
                    
                    outfile = '/eos/user/s/sxiaohe/OpenData/MC2015/StandardModelPhysics/{}/{}_{}.json'.format(process, dname, recid)
                    with open(outfile, 'w') as jsonfile:
                        json.dump(metadata, jsonfile)
                        print("Saved to {}".format(outfile))
            except:
                print("Saving to json failed {} due to an unexpected error".format(fname))
