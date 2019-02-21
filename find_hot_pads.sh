#!/bin/bash

printf '%7s %-3s\t%-3s\t%-1s\t%-2s\t%-2s\n' "freq." "sec" "row" "loc" "loc" "pwb" > $1.srt

sort -k1 -k2 -g $1 | uniq -c | sort -r -g >> $1.srt

head $1.srt
