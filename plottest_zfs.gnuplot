set datafile separator ","
#set terminal png size 900,400
set title "R/W Test"
set ylabel "R/W Speed"
set xlabel "Date"
set xdata time
set timefmt "%s"
set format x "%H:%M:%S"
set key left top
set grid
plot "< tail -100 /tmp/testread.dat" using 1:2 with lines lw 2 lt 3 title 'read [GB/s]', \
     "< tail -100 /tmp/testwrite.dat" using 1:2 with lines lw 2 lt 1 title 'write [MB/s]'
pause 100
reread