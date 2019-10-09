#!/bin/bash

while :
do
    echo "miao" > /daq/alpha_data0/acapra/alphag/miao.txt
    sleep 1
    echo $RANDOM >> /daq/alpha_data0/acapra/alphag/miao.txt
    sleep 1
    echo "bye" >> /daq/alpha_data0/acapra/alphag/miao.txt
    sleep 1
    rm -f /daq/alpha_data0/acapra/alphag/miao.txt
    sleep 2
done
