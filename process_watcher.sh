#!/bin/bash

var=$1

if [[ $var =~ ^-?[0-9]+$ ]]; then 
    pid=$var
    echo "${pid} is a valid PID"
else 
    pid=$(pidof $var)
    echo "program \"${var}\" has PID ${pid}"
fi

echo "Start Watching " $pid

while kill -0 $pid; do 
    sleep 1
done


echo "Process with PID ${pid} is completed" | mail -s "Process $var" andrea.capra85@gmail.com
