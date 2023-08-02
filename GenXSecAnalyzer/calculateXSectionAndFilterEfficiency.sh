FILE='DYJetsToLL.txt'
DATANAME='DYJetsToLL'
EVENTS='1000000'

SKIPEXISTING=False

while getopts f:d:n:s option
do
    case "${option}"
    in
            f) FILE=${OPTARG};;
            d) DATANAME=${OPTARG};;
            n) EVENTS=${OPTARG};;
            s) SKIPEXISTING=True;;
    esac
done

echo 'compute_cross_section.py -f '${FILE}' -d '${DATANAME}' -n '${EVENTS}' --skipexisting "'${SKIPEXISTING}'"'
output="$(python compute_cross_section.py -f "${FILE}" -d "${DATANAME}" -n "${EVENTS}" --skipexisting "${SKIPEXISTING}")"
output="${output#*.txt}"
output="${output#*.txt}"

if [[ $output == *"cmsRun"* ]]; then
    eval ${output}
else
    echo ${output}
fi
echo ""

python output_to_numpy.py
