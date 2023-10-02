import os,sys,shutil,datetime,time, subprocess
import StandardModelPhysics

start_time = time.time()

filesPerJob = 999

runDir=os.getcwd()
cTime=datetime.datetime.now()
date='%i_%i_%i_%i_%i_%i'%(cTime.year,cTime.month,cTime.day,cTime.hour,cTime.minute,cTime.second)

print ('--- Starting Submission ---')

# --- Check sample size and aim for <= 50GB per job
command = '/cvmfs/cms.cern.ch/common/dasgoclient --query="dataset dataset=/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM | grep dataset.size" '
proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
(out, err) = proc.communicate()
try: 
    samplesize = int(out.split('\n')[0])
except:    
    try: 
        samplesize = int(out.split('\n')[1])
    except:
        try: 
            samplesize = int(out.split('\n')[2])
        except: 
            print 'need more than 2 levels to get sample size'
            exit(1)
            
jobsPerSample = max(1,round(samplesize/50000000000.))
