<details>
<summary><h3>2015</h3></summary>
<p>
Location of the json files: <code>/eos/user/s/sxiaohe/OpenData/MC2015/<em>Section</em>/<em>Subsection</em></code>

e.g.: <code>/eos/user/s/sxiaohe/OpenData/MC2015/StandardModelPhysics/Drell-Yan</code> for all Standard Model Drell-Yan samples
</p>

<p>
The Section and Subsection names can be found on Open Data Portal http://opendata.cern.ch/search?page=1&size=20&experiment=CMS&subtype=Simulated&type=Dataset&year=2015
</p>

<p>
Folder Hierarchy:
 
* <code>MC2015/</code>

 * <code>StandardModelPhysics/</code>
 
  * <code>Drell-Yan/</code>
  * <code>ElectroWeak/</code>
  * <code>MinimumBias/</code>
  * <code>QCD/</code>
  * <code>TopPhysics/</code>
    
Under each subfolder, the json files are stored under the name <sample_name>_<recid>.json. (e.g. DYJetsToLL_M-100to200_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_16426.json)
</p>
<p>
  
* Finished Section: StandardModelPhysics
  
  * Subsections: Drell-Yan, ElectroWeak, QCD, TopPhysics, MinimumBias
    
* Section in progress: HiggsPhysics (Low priority)
</p>
</details>

<details>
<summary><h3>2016</h3></summary>
Location of the json files: /eos/user/s/sxiaohe/OpenData/MC2016/<Section>/<Subsection>/
  
</details>

# OpenData
Runs GenXSecAnalyzer and stores the result in json files


## Access the data in the output files:
### Loading the output json files:
import json

f = open('<sample_name>_<recid>.json')
data = json.load(f)

### To access the full name and description of the dataset:
data["Dataset"]
It will return a string in format:
/DYJetsToLL_M-100to200_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM

### To access a specific value:
result["<column_name>"] for value
result["<column_name_err>"] for error

#### Available column names:
GenXSecAnalyzer gives outputs in 3 possible formats (some information is not available for some datasets).

Format 1:
- "totX_beforeMat":"Total cross section before matching (pb)",
- "totX_beforeMat_err":"(+-) Error of total cross section before matching (pb)",
- "totX_afterMat":"Total cross section after matching (pb)",
- "totX_afterMat_err":"(+-) Error of total cross section after matching (pb)",
- "matchingEff":"Matching efficiency",
- "matchingEff_err":"(+-) Error of matching efficiency",
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

### To run the GenXSecAnalyhzer:
### Prepare the input filelists for the GenXSecAnalyzer
python makeFileLists.py [physics_process]

e.g. python makeFileLists.py Drell-Yan
Choose from: Drell-Yan / ElectroWeak / MinimumBias / QCD / TopPhysics

Running this command results .txt files in the fileLists/ folder. Each recid_{id}.txt file contains the address of all the files under that recid.

### Setup the environment (lxplus)
To use slc6 on Singularity (need to execute everytime when you login):
cmssw-el6

To download the CMSSW folder (only need to execute once): (CMSSW_7_6_7 is recommended for MC2015)
cmsrel CMSSW_7_6_7

To setup the CMSSW environment (need to execute everytime when you login):
cd CMSSW_7_6_7/src
cmsenv

##### To run on a single dataset:
./calculateXSectionAndFilterEfficiency.sh -f <list_of_root_files.txt> -s <section_name> -p <subsection_name> -n <maximum_num_of_events> -k <True_to_skipExistingLogFiles/False_to_NOT_skipExistingLogFiles>

e.g.: ./src/calculateXSectionAndFilterEfficiency.sh -f recid_16785.txt -s StandardModelPhysics -p Drell-Yan -n 10000 -k False
Set maximum number of events to -1 to run all the events in each root file
In the example, recid_16785.txt contains a list of root files in the format of "root://eospublic.cern.ch//eos/opendata/".

If you get an error saying "Permisson denied", type "chmod 777 calculateXSectionAndFilterEfficiency.sh" to give the permission to the .sh file first and then rerun the above command.

##### To run all the datasets under a category (Drell-Yan / ElectroWeak / MinimumBias / QCD / TopPhysics):
python src/runRecursive.py <Section> <Subsection>

e.g.: python src/runRecursive.py StandardModel Drell-Yan

If we already have .log files, we can run "python output_to_json.py recid_16785.txt StandardModel Drell-Yan" by itself to get the json files, with the second argument being consistent with the name of the destination directory.

output_to_numpy.py and output_to_csv.py, which coverts the log files into numpy and csv files, have not been updated yet.

#### For numpy outputs (OUTDATED):
To use the output of the GenXSecAnalyzer, we only need to do:
import numpy as np
result = np.load("<dataset_name>.npy")

The output is a 16 column array.
To access the columns:
result["<column_name>"][0] for value
result["<column_name>"][1] for error
e.g. result["totX_final"] gives the value of the final total cross section
     result["totX_final_err"] gives its error

To check all the metadata:
print(result.dtype.metadata)

To check the metadata for a specific column:
print(xsec_arr.dtype.metadata["<column_name>"])
e.g.: print(xsec_arr.dtype.metadata["equivLumi"])

#### Note:
output_to_numpy.py and output_to_csv.py have not been updated to be compatible with the most recent changes.
