#!/bin/bash

IFS=$'\n'

for IMG in `find .. -name *.jpg`; do
#    echo $IMG
    LNK=`basename $IMG`
    echo $LNK
    ln -s $IMG $PWD/$LNK
done
