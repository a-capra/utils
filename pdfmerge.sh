#!/bin/bash    

GHOSTSCRIPT=$(which gs 2> /dev/null)
if [ "$GHOSTSCRIPT" == ""  ];then
    echo "GHOSTSCRIPT not available in your system"
    echo "(install as root) yum install ghostscript"
    exit 123
fi

echo "[ /Title ($1)" > pdfmarks
echo "  /Author (Andrea Capra)" >> pdfmarks
echo "  /ModDate (D:`date +%Y%m%d%H%M`)" >> pdfmarks
echo "  /CreationDate (D:`date +%Y%m%d%H%M`)" >> pdfmarks
echo "  /Creator (Andrea Capra on Linux)" >> pdfmarks
echo "  /Producer (gs)" >> pdfmarks
echo "  /DOCINFO pdfmark" >> pdfmarks

if [ $# -lt 3 ]; then
	echo "Usage"
	echo "pdfmerge.sh outfile.pdf infile1.pdf infile2.pdf ... infileN.pdf"
	rm -f pdfmarks
	exit 1
elif [ $# -eq 3 ]; then
	gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=$1 $2 $3
	echo $1 '<--' $2 '+' $3
	exit 0
else
	i=1
	for arg in "$@"
	do
		IF[$i]=$arg
		#echo $i ${IF[$i]}
	let i=i+1
	done

	gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=pdf3.temp $2 $3
	echo pdf3.temp '<--' $2 '+' $3
	j=4
	TF=pdf3.temp
	while [ $j -lt ${#IF[@]} ]; do
			TF=pdf$j.temp
			gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=$TF pdf$((j-1)).temp ${IF[$j]}
			echo pdf$j.temp '<--' pdf$((j-1)).temp '+' ${IF[$j]}
	let j=j+1
	done
	gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=$1 $TF ${IF[${#IF[@]}]}
	echo $1 '<--' $TF '+' ${IF[${#IF[@]}]}
	rm -f pdf*.temp
fi

rm -f pdfmarks

echo `ls $1` "CREATED!"
