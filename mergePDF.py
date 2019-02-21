#!/usr/bin/env python3

import PyPDF2
import sys
import os.path as op

if __name__=='__main__':

        pdfWriter = PyPDF2.PdfFileWriter()
        argc=len(sys.argv)
        #print('argc =',argc)
        if argc<4:
                print('Usage:\tmergePDF.py output.pdf input1.pdf input2.pdf ...')
                sys.exit(1)
        for fpdf in sys.argv[2:argc]:
                if not op.isfile(fpdf):	
                        print(fpdf,' does not exist... skipping')
                        continue
                f = open(fpdf, 'rb')
                print('-->',fpdf)
                pdfReader = PyPDF2.PdfFileReader(f)
                print('pages:',pdfReader.numPages)
                for pageNum in range(pdfReader.numPages):
                        pageObj = pdfReader.getPage(pageNum)
                        pdfWriter.addPage(pageObj)

        pdfOutputFile = open(sys.argv[1], 'wb')
        pdfWriter.write(pdfOutputFile)
        pdfOutputFile.close()
	
