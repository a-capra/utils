#!/bin/bash

dir="../Documents/ALPHA-2/SME"
for f in `ls .`; do
    if [[ ! -e "$dir/$f" ]]; then
        continue
    fi 
    #ls -lh --color $f "$dir/$f"
    out=$(diff $f "$dir/$f")
    if [[ -z $out ]]; then
        echo $f "is up-to-date"
    else
        echo "kompare $f $dir/$f"
        kompare $f "$dir/$f" &> /dev/null &
    fi
done
