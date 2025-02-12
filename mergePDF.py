#!/usr/bin/env python3

import PyPDF2
import sys
import os.path as op

if __name__=='__main__':

        pdfWriter = PyPDF2.PdfWriter()
        argc=len(sys.argv)
        
        if argc<4:
                print('Usage:\nmergePDF.py output.pdf input1.pdf input2.pdf ...')
                sys.exit(1)
        for fpdf in sys.argv[2:argc]:
                if not op.isfile(fpdf):	
                        print(fpdf,' does not exist... skipping')
                        continue
                f = open(fpdf, 'rb')
                print('-->',fpdf)
                pdfReader = PyPDF2.PdfReader(f)
                print('pages:',len(pdfReader.pages))
                for pageNum in range(len(pdfReader.pages)):
                        pageObj = pdfReader.pages[pageNum]
                        pdfWriter.add_page(pageObj)

        pdfOutputFile = open(sys.argv[1], 'wb')
        pdfWriter.write(pdfOutputFile)
        pdfOutputFile.close()
	
