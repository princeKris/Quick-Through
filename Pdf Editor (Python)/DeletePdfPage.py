from PyPDF2 import PdfWriter, PdfReader
print("\n\n")
print(" Delete PDF Pages".center(40,"+"))
inputpdf=input("Enter The PDF File Path : ")
deletedpages=input("Enter The Page Number You Want To Delete using , (1,2,5) : ").split(",")
outputpdf=input("Enter The Output PDF File Name : ")
pdfreader=PdfReader(inputpdf,'rb')
pdfwriter=PdfWriter()
for i in range(len(pdfreader.pages)):
    if(str(i+1) not in deletedpages):
        pdfwriter.add_page(pdfreader.pages[i])
with open(f'{outputpdf}.pdf', 'wb') as f:
    pdfwriter.write(f)