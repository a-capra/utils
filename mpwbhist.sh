#!/bin/bash

varlist=("sfp_rx_power" "sfp_tx_power" "sfp_tx_bias")

echo "cd /History/Display" > mpwbhist.com

for c in `seq 0 7`; do
    echo "cd /History/Display" > mpwbhist.com
    echo "mkdir PWBcol${c}" >> mpwbhist.com
    echo "cd PWBcol${c}" >> mpwbhist.com
    for var in varlist; do
	echo "mkdir $var" >> mpwbhist.com
	echo "cd $var" >> mpwbhist.com

	create string Variables[8][64]
	create string Label[8][32]
	set Variables[r] CTRL/pwb_sfp_rx_power:pwb_sfp_rx_power[i]
	set Label[r] "row$r"

	create float Minimum 
	set Minimum 0
	create float Maximum 
	set Maximum 0
	
	create bool "Show values"
	set "Show values" 1
	create bool "Show run markers"
	set "Show run markers" 0
	
	create float Factor
	set Factor[*] 1
	create float Offset
	set Offset[*] 0
	
	create string Timescale[1][32]
	set Timescale "1h"
	
	create bool "Zero ylow"
	set "Zero ylow" 1
	create bool "Log axis"
	set "Log axis" 0

	create bool "Sort vars"
	set "Sort vars" 0
	create bool "Show old vars"
	set "Show old vars" 0
	cd ..
	done
    cd /
done


CTRL/pwb_sfp_rx_power:pwb_sfp_tx_power[]
CTRL/pwb_sfp_rx_power:pwb_sfp_tx_bias[]
CTRL/pwb_v_sca12:pwb_v_sca12[]
CTRL/pwb_v_sca34:pwb_v_sca34[]
CTRL/pwb_i_sca12:pwb_i_sca12[]
CTRL/pwb_i_sca34:pwb_i_sca34[]
