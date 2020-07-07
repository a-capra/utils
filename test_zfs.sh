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
    echo "$timestamp,$duration" >> /tmp/testwrite.dat
    echo "sleep now"
    sleep 5

    echo "test read:"
    timestamp=$(date +%s)
    dd if=$tempfile of=/dev/null bs=1M count=1024 2> /tmp/testread.log
    cat /tmp/testread.log
    duration=$(tail -1 /tmp/testread.log | awk '{print $6}')
    echo "$timestamp,$duration" >> /tmp/testread.dat
    echo "sleep now"
    sleep 5
done

