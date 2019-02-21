#!/bin/bash

if [ $# != 2 ]; then
    echo "Usage:"
    echo "snooze <repetition> <minutes>"
    exit 123
fi

rep=$1
min=$2

r=1
while [ $r <= $rep ]; do
    at now + $min -f /tmp/.myjob
    rep=$(( $rep + 1 ))
done
