from PyPDF2 import PdfFileReader
import argparse

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('fin',type=argparse.FileType('rb'),help="input PDF")
    args = parser.parse_args()
    
    reader = PdfFileReader(args.fin)
    #metadata = reader.getDocumentInfo()
    #print(metadata)

    meta = reader.metadata
    print(f"Author: {meta.author}, Title: {meta.title}")
    