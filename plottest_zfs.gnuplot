set datafile separator ","
#set terminal png size 900,400
set title "R/W Test"
set ylabel "R/W time in seconds"
set xlabel "Date"
set xdata time
set timefmt "%s"
set format x "%H:%M:%S"
set key left top
set grid
plot "< tail -20 /tmp/testread.dat" using 1:2 with lines lw 2 lt 3 title 'read', \
     "< tail -20 /tmp/testwrite.dat" using 1:2 with lines lw 2 lt 1 title 'write'
pause 10
reread