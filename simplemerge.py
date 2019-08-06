import PyPDF2
import os
import os.path as op

if __name__=='__main__':

	pdfWriter = PyPDF2.PdfFileWriter()
	xxx=20190806
	for n in range(1,17):
		fname='Scan_%d_%d.pdf'%(xxx,n)
		if not op.isfile(fname):
			continue
		fpdf=open(fname, 'rb')
		print(n,fname)
		pdfReader = PyPDF2.PdfFileReader(fpdf)
		print('pages:',pdfReader.numPages)
		for pageNum in range(pdfReader.numPages):
			pageObj = pdfReader.getPage(pageNum)
			pdfWriter.addPage(pageObj)

	pdfOutputFile = open('merged.pdf', 'wb')
	pdfWriter.write(pdfOutputFile)
	pdfOutputFile.close()

	