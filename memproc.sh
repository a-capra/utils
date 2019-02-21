#!/bin/bash

TYPE=("Rss" "Shared" "Private" "Swap" "Pss")
# Rss: resident memory usage, all memory the process uses, including all memory this process shares with other processes. It does not include swap;
# Shared: memory that this process shares with other processes;
# Private: private memory used by this process, you can look for memory leaks here;
# Swap: swap memory used by the process;
# Pss: Proportional Set Size, a good overall memory indicator. It is the Rss adjusted for sharing: if a process has 1MiB private and 20MiB shared between other 10 processes, Pss is 1 + 20/10 = 3MiB

PROCESS_NAME=$1
n=$2

i=0
for PID in `pidof ${PROCESS_NAME}`; do
    PID_LIST[$i]=$PID
#    echo $i ${PID_LIST[$i]}
    i=$((i+1))
done


echo "Finding ${TYPE[$n]} type memory usage for ${PROCESS_NAME}"
echo " --- PID: ${PID_LIST[0]}"


MEM=$(echo 0 $(cat /proc/${PID_LIST[0]}/smaps | grep "${TYPE[$n]}" | awk '{print $2}' | sed s#^#+# ) | bc)
UNIT=$(cat /proc/${PID_LIST[0]}/smaps | grep "${TYPE[$n]}" | awk '{print $3}' | tail -1)
echo '***   ' ${MEM} ' ' ${UNIT} '   ***'

echo '***   ' `units -t "${MEM} ${UNIT}" GB` ' GB    ***'
