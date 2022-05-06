#!/bin/bash

tempfile=$1
trap "rm -f $tempfile; echo bye; exit 0"  2
rm -f /tmp/testwrite.dat /tmp/testread.dat
while :
do
    sync

    echo "test write:"
    timestamp=$(date +%s)
    dd if=/dev/zero of=$tempfile bs=1M count=1024 oflag=dsync 2> /tmp/testwrite.log
    cat /tmp/testwrite.log
    duration=$(tail -1 /tmp/testwrite.log | awk '{print $6}')
    #speed=$(echo "1024/$duration" | bc -l)
    speed=$(tail -1 /tmp/testwrite.log | awk '{print $8}')
    echo "$timestamp,$speed,$duration" >> /tmp/testwrite.dat
    echo "sleep now"
    sleep 5

    echo "test read:"
    timestamp=$(date +%s)
    dd if=$tempfile of=/dev/null bs=1M count=1024 2> /tmp/testread.log
    cat /tmp/testread.log
    duration=$(tail -1 /tmp/testread.log | awk '{print $6}')
    speed=$(tail -1 /tmp/testread.log | awk '{print $8}')
    #speed=$(echo "1.1/$duration" | bc -l)
    echo "$timestamp,$speed,$duration" >> /tmp/testread.dat
    echo "sleep now"
    sleep 5
done

