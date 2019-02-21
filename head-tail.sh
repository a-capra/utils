#!/bin/bash
IFS=$'\n'
#exaple directory
DIR="/home/andrea/"
N=$(ls ${DIR} | cat | wc -l)
echo "Number of Files: $N"
G=10
echo "Number of grous: $G"
M=1

i=$(echo "$N/$G" | bc)
j=$i
echo "Number parallel operations: $i"

while [ $i -le $N ]; do
    echo "group ${M})  file index up to ${i}"
    ls ${DIR} | cat | head -${i} | tail -${j}
    for FILE in `ls ${DIR} | cat | head -${i} | tail -${j}`; do
       echo "---> ${DIR}${FILE}"
       # do something ${DIR}${FILE} &
    done
    #wait $!
    i=$((i+j))
    M=$((M+1))
    echo "------------------------------------------"
done
