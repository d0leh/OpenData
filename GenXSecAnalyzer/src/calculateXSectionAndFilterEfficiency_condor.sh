#!/bin/bash

FILE=${1}
DATANAME=${2}
EVENTS=${3}

SKIPEXISTING=False

source /cvmfs/cms.cern.ch/cmsset_default.sh
scramv1 project CMSSW CMSSW_7_6_7
cd CMSSW_7_6_7
cmsenv

echo 'python src/compute_cross_section.py -f '${FILE}' -d '${DATANAME}' -n '${EVENTS}' --skipexisting "'${SKIPEXISTING}'"'
output="$(python src/compute_cross_section.py -f "${FILE}" -d "${DATANAME}" -n "${EVENTS}" --skipexisting "${SKIPEXISTING}")"
output="${output#*.txt}"
output="${output#*.txt}"

if [[ $output == *"cmsRun"* ]]; then
    eval ${output}
else
    echo ${output}
fi
echo ""

python src/output_to_json.py
