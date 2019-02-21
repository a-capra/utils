#!/bin/bash

DATA=/home/alpha/andrea/data
RUNNO="02284"
LEAKLOG="R${RUNNO}.memtest.log"
LEAKOUT="R${RUNNO}.val.log"

#valgrind --leak-check=full --error-limit=no --suppressions=${ROOTSYS}/etc/valgrind-root.supp  --log-file="${LEAKLOG}" ./agana.exe ${DATA}/run${RUNNO}sub010.mid.lz4 &> ${LEAKOUT}
valgrind --leak-check=full --error-limit=no --suppressions=${ROOTSYS}/etc/valgrind-root.supp  --log-file="${LEAKLOG}" ./agana.exe ${DATA}/run${RUNNO}sub010.mid.lz4
