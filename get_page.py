import PyPDF2
import argparse

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('fin',type=argparse.FileType('rb'),help="input PDF")
    parser.add_argument('fout',type=argparse.FileType('wb'),help="output PDF")
    parser.add_argument('-p','--pages',type=int,nargs ='+',help ='an integer for the accumulator')
    args = parser.parse_args()
    if min(args.pages) < 1: raise ValueError

    pdfWriter = PyPDF2.PdfFileWriter()
    
    pdfReader = PyPDF2.PdfFileReader(args.fin)
    for page in args.pages:
        pageObj = pdfReader.getPage(page-1)
        pdfWriter.addPage(pageObj)
    
    pdfWriter.write(args.fout)
    args.fout.close()
