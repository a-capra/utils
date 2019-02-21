#!/bin/bash

while read -r run; do
    scp /alpha/agdaq/data/run0${run}* alpha@alphabeast01:/mnt/data_drive/andrea/data
done < $1
