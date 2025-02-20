while getopts f:y:s:p:n:k: option
do
    case "${option}" in
	f) FILE=${OPTARG};;
	y) YEAR=${OPTARG};;
        s) SECTIONNAME=${OPTARG};;
	p) PROCESSNAME=${OPTARG};;
        n) EVENTS=${OPTARG};;
        k) SKIPEXISTING=${OPTARG};;
    esac
done

echo "python src/compute_cross_section.py -f '${FILE}' -y '${YEAR}' -s '${SECTIONNAME}' -p '${PROCESSNAME}' -n '${EVENTS}' -k '${SKIPEXISTING}'"
output="$(python src/compute_cross_section.py -f "${FILE}"  -y "${YEAR}" -s "${SECTIONNAME}" -p "${PROCESSNAME}" -n "${EVENTS}" -k "${SKIPEXISTING}")"
output="${output#*.txt}"
output="${output#*.txt}"

if [[ $output == *"cmsRun"* ]]; then
    eval ${output}
else
    echo ${output}
fi
echo ""

#python2 src/output_to_json_DAS.py "${FILE}" "${YEAR}" "${SECTIONNAME}" "${PROCESSNAME}"
