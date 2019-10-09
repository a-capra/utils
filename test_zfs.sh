#!/bin/bash

tempfile=$1
trap "rm -f $tempfile; echo bye; exit 0"  2
while :
do
    sync
    echo "test write:"
    dd if=/dev/zero of=$tempfile bs=1M count=1024 oflag=dsync
    echo "sleep now"
    sleep 5
    echo "test read:"
    dd if=$tempfile of=/dev/null bs=1M count=1024
    echo "sleep now"
    sleep 5
done
