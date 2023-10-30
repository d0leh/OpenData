while getopts f:s:p:n:k: option
do
    case "${option}" in
	f) FILE=${OPTARG};;
        s) SECTIONNAME=${OPTARG};;
	p) PROCESSNAME=${OPTARG};;
        n) EVENTS=${OPTARG};;
        k) SKIPEXISTING=${OPTARG};;
    esac
done

echo "python src/compute_cross_section.py -f '${FILE}' -s '${SECTIONNAME}' -p '${PROCESSNAME}' -n '${EVENTS}' -k '${SKIPEXISTING}'"
output="$(python src/compute_cross_section.py -f "${FILE}" -s "${SECTIONNAME}" -p "${PROCESSNAME}" -n "${EVENTS}" -k "${SKIPEXISTING}")"
output="${output#*.txt}"
output="${output#*.txt}"

if [[ $output == *"cmsRun"* ]]; then
    eval ${output}
else
    echo ${output}
fi
echo ""

python src/output_to_json.py "${FILE}" "${SECTIONNAME}" "${PROCESSNAME}"
