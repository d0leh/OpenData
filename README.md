# Overview
A collection of scripts that run GenXSecAnalyzer and store the result in json files.

Use different scripts to process samples for different years.

<details>
<summary><h2>2015</h2></summary>

  <b>Location</b> of the json files: <code>/eos/user/s/sxiaohe/OpenData/MC2015/<em>Section</em>/<em>Subsection</em></code>

  e.g.: <code>/eos/user/s/sxiaohe/OpenData/MC2015/StandardModelPhysics/Drell-Yan</code> for all Standard Model Drell-Yan samples

  The Section and Subsection names can be found on Open Data Portal http://opendata.cern.ch/search?page=1&size=20&experiment=CMS&subtype=Simulated&type=Dataset&year=2015

  <break>

  <details>
  <summary> <b>Folder Hierarchy:</b></summary>  
  <ul>
  <li>MC2015/
    <ul>
      <li>StandardModelPhysics/
        <ul>
          <li>Drell-Yan/</li>    
          <li>ElectroWeak/</li>
          <li>MinimumBias/</li>
          <li>QCD/</li>
          <li>TopPhysics/</li>
        </ul>
      </li>
      <li>HiggsPhysics/
        <ul>
          <li>BeyondStandardModel/</li>
          <li>StandardModel/</li>
        </ul>
      </li>
    </ul>
  </li>
  </ul>
  </details>
    
  Under each subfolder, the json files are stored under the name <code><em>sample_name</em>_<em>recid</em>.json</code>.

  (e.g. <code>DYJetsToLL_M-100to200_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_16426.json</code>)  

  <break>
  
  * Finished Section: StandardModelPhysics
  
    * Subsections: Drell-Yan, ElectroWeak, QCD, TopPhysics, MinimumBias
    
  * Section in progress: HiggsPhysics (Low priority)

  <details>
  <summary><b>Access the data in the output files:</b></summary>
    Loading the output json files:</b>
    <pre>
      <code>
        import json
        f = open('<em>sample_name_recid</em>.json')
        data = json.load(f)
      </code>
    </pre>
  </details>

  <details>
    <summary><b>To access the full name the dataset:</b></summary>
      <code>data["Dataset"]</code>
      It will return a string in format:
      <code>/DYJetsToLL_M-100to200_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM</code>
  </details>

  <details>
    <summary><b>To access stored values (e.g. total cross section, ...):</b></summary>
      <code>result["<em>column_name</em>"]</code> for value
      <code>result["<em>column_name_err</em>"]</code> for error
  </details>

  <details>
      <summary><b>Available column names:</b></summary>
        GenXSecAnalyzer gives outputs in 5 possible formats (some information is not available for some datasets).

        Format 1:
        
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
        "equivLumi_err":"(+-) Error of final equivalent lumi for 1M events (1/fb)"
        
        Format 2:
        
        - "totX_beforeMat":"Total cross section before matching (pb)",
        - "totX_beforeMat_err":"(+-) Error of total cross section before matching (pb)",
        - "totX_afterMat":"Total cross section after matching (pb)",
        - "totX_afterMat_err":"(+-) Error of total cross section after matching (pb)",
        - "filterEff_weights":"Filter efficiency (taking into account weights)",
        - "filterEff_weights_err":"(+-) Error of filter efficiency (taking into account weights)",
        - "filterEff_event":"Filter efficiency (event-level)",
        - "filterEff_event_err":"(+-) Error of filter efficiency (event-level)",
        - "totX_final":"Final cross senction after filter (pb)",
        - "totX_final_err":"(+-) Error of final cross section after filter (pb)"
        
        Format 3:
        
        - "totX_beforeFilter":"Total cross section before filter (pb)",
        - "totX_beforeFilter_err":"(+-) Error of total cross section before filter (pb)",
        - "filterEff_weights":"Filter efficiency (taking into account weights)",
        - "filterEff_weights_err":"(+-) Error of filter efficiency (taking into account weights)",
        - "filterEff_event":"Filter efficiency (event-level)",
        - "filterEff_event_err":"(+-) Error of filter efficiency (event-level)",
        - "totX_final":"Final cross senction after filter (pb)",
        - "totX_final_err":"(+-) Error of final cross section after filter (pb)",
        - "negWeightFrac":"Final fraction of events with negative weights after filter",
        - "negWeightFrac_err":"(+-) Error of final fraction of events with negative weights after filter",
        - "equivLumi":"Final equivalent lumi for 1M events (1/fb)",
        - "equivLumi_err":"(+-) Error of final equivalent lumi for 1M events (1/fb)"
        
        Format 4:
        
        - "totX_beforeFilter":"Total cross section before filter (pb)",
        - "totX_beforeFilter_err":"(+-) Error of total cross section before filter (pb)",
        - "filterEff_weights":"Filter efficiency (taking into account weights)",
        - "filterEff_weights_err":"(+-) Error of filter efficiency (taking into account weights)",
        - "filterEff_event":"Filter efficiency (event-level)",
        - "filterEff_event_err":"(+-) Error of filter efficiency (event-level)",
        - "totX_final":"Final cross senction after filter (pb)",
        - "totX_final_err":"(+-) Error of final cross senction after filter (pb)"
        
        Format 5:
        
        - "filterEff_weights":"Filter efficiency (taking into account weights)",
        - "filterEff_weights_err":"(+-) Error of filter efficiency (taking into account weights)",
        - "filterEff_event":"Filter efficiency (event-level)",
        - "filterEff_event_err":"(+-) Error of filter efficiency (event-level)",
        - "totX_final":"Final cross senction after filter (pb)",
        - "totX_final_err":"(+-) Error of final cross senction after filter (pb)"
        
        
  </details>
   
  
  <details>
    <summary><b>To run the GenXSecAnalyzer:</b></summary>

      * Prepare the input filelists for the GenXSecAnalyzer
      
          <code>python makeFileLists.py [physics_process]</code>
        
          e.g. <code>python makeFileLists.py Drell-Yan</code>
          
          Choose from: <code>Drell-Yan / ElectroWeak / MinimumBias / QCD / TopPhysics</code>
          
          Running this command results .txt files in the fileLists/ folder. Each recid_{id}.txt file contains the address of all the files under that recid.
      
      * Setup the environment (lxplus)
        
          To use slc6 on Singularity (need to execute everytime when you login):
          <code>cmssw-el6</code>
      
          To download the CMSSW folder (only need to execute once): (CMSSW_7_6_7 is recommended for MC2015)
          <code>cmsrel CMSSW_7_6_7</code>
      
          To setup the CMSSW environment (need to execute everytime when you login):
          <pre>
            <code>
              cd CMSSW_7_6_7/src
            cmsenv
            </code>
          </pre>
    
        * To run on a single dataset:
        
            <code>./calculateXSectionAndFilterEfficiency.sh -f <em>list_of_root_files.txt</em> -s <em>section_name</em> -p <em>subsection_name</em> -n <em>maximum_num_of_events</em> -k <em>skipExistingLogFiles</em></code>
            
            e.g.: <code>./src/calculateXSectionAndFilterEfficiency.sh -f recid_16785.txt -s StandardModelPhysics -p Drell-Yan -n 10000 -k False</code>
      
            Set maximum number of events to -1 to run all the events in each root file.
      
            In the example, <code>recid_16785.txt</code> contains a list of root files in the format of <code>"root://eospublic.cern.ch//eos/opendata/"</code>.
      
            If you get an error saying "</code>Permisson denied</code>", run <code>chmod 777 calculateXSectionAndFilterEfficiency.sh</code> to give the permission to the .sh file first and then rerun the above command.
      
        * To run all the datasets under a category (Drell-Yan / ElectroWeak / MinimumBias / QCD / TopPhysics):
      
           <code>python src/runRecursive.py <em>Section</em> <em>Subsection</em></code>
      
           e.g.: <code>python src/runRecursive.py StandardModel Drell-Yan</code>
      
           If we already have <code>.log</code> files, we can run <code>python output_to_json.py recid_16785.txt StandardModel Drell-Yan</code> by itself to get the json files, with the second argument being consistent with the name of the destination directory.
  </details>
  
</details>

<details>
<summary><h2>2016</h2></summary>
Location of the json files: /eos/user/s/sxiaohe/OpenData/MC2016/<Section>/<Subsection>/
</details>








