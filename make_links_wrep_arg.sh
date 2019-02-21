#!/bin/bash

IFS=$'\n'

BASEDIR=$1
LINKDIR=$2

i=0
for IMG in `find ${BASEDIR} -name *.jpg`; do
    echo $IMG
    LNK=`basename $IMG`
    echo $LNK
    if [ -e "$LINKDIR/$LNK" ]; then
	NAME=`basename $LNK .jpg`
	LNK=${NAME}_${i}.jpg
	i=$((i+1))
    fi
    ln -s $IMG $LINKDIR/$LNK
done
