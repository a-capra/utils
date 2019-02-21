#!/bin/bash

while read -r line; do 
    banks=()
    read -r -a banks <<< "$line"
    odbedit -c "create string /Equipment/Labview/Settings/BankNames/${banks[0]}"
    echo -n ${banks[0]}
    if [[ ${banks[1]} == "" ]] ;then
	echo " ***"
     else
	odbedit -c "set /Equipment/Labview/Settings/BankNames/${banks[0]} ${banks[1]}"
	echo " " ${banks[1]}
     fi
done < "labviewbanks.txt"
