#SKIPEXISTING=False

while getopts f:d:n:s option
do
    case "${option}"
    in
            f) FILE=${OPTARG};;
            s) SECTIONNAME=${OPTARG};;
	    p) PROCESSNAME=${OPTARG};;
            n) EVENTS=${OPTARG};;
            k) SKIPEXISTING=False;;
    esac
done

echo "python src/compute_cross_section.py -f '${FILE}' -s '${SECTIONNAME}' -p '${PROCESSNAME}' -n '${EVENTS}' --skipexisting '${SKIPEXISTING}'"
output="$(python src/compute_cross_section.py -f "${FILE}" -d "${DATANAME}" -n "${EVENTS}" --skipexisting "${SKIPEXISTING}")"
output="${output#*.txt}"
output="${output#*.txt}"

if [[ $output == *"cmsRun"* ]]; then
    eval ${output}
else
    echo ${output}
fi
echo ""

python src/output_to_json.py "${FILE}" "${SECTIONNAME}" "${PROCESSNAME}"
