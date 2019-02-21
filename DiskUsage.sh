#!/bin/bash

FNAME="diskusage_`date +%F_%H%M%S`.log"
du -h | sort -h -r > ${FNAME}

head -35 ${FNAME}

echo -e "\nList at" ${FNAME}
