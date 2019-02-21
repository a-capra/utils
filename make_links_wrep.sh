#!/bin/bash

IFS=$'\n'

i=0
for IMG in `find .. -name *.jpg`; do
    echo $IMG
    LNK=`basename $IMG`
    echo $LNK
    if [ -e "$PWD/$LNK" ]; then
	NAME=`basename $LNK .jpg`
	LNK=${NAME}_${i}.jpg
	i=$((i+1))
    fi
    ln -s $IMG $PWD/$LNK
done
