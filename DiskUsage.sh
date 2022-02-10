#!/bin/bash

FNAME="diskusage_`date +%F_%H%M%S`.log"
# disk usage in human readable form '-h'
#     "      only one filesystem '-x'
# reverse sort '-r' 
# using human readable numbers '-h'
du -h -x | sort -h -r > ${FNAME}

head -35 ${FNAME}

echo -e "\nList at" ${FNAME}
