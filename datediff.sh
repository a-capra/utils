#!/bin/bash

datediff() {
    d1=$(date -d "$1" +%s)
    d2=$(date -d "$2" +%s)
    echo $(( (d1 - d2) / 86400 )) days
}

echo "Example: datediff '1 Nov' '1 Aug'"
datediff "$1" "$2"
