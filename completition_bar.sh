#!/bin/bash

frac=0

while [ $frac  100 ]; do
    frac=$(echo "`grep "Event" RunLogs/run.log | wc -l`/10000*100" | bc -l)
    echo -ne "${frac}%\r"
    sleep 1
done
