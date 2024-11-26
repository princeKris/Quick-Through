from PyPDF2 import PdfMerger,PdfReader
import os
pdfMerge = PdfMerger()
print("\n\n\n")
print(" PDF Merger ".center(40,"+"))
print("1.Enter The Pdf Files You Want Merge (tes1.pdf,tes2.pdf,tool.pdf)\n2.Enter The Folder Path To Merge The all PDF Files in The Folder (C:\\ltesr\\loder)")
try:
    Opt=str(input("Enter The Input : ")).split(",")
    outputpdf=str(input("Enter The Output Pdf File Name : "))
    if(len(Opt)>1):
        for i in Opt:
            pdfFile = open(i, 'rb')
            pdfReader = PdfReader(pdfFile)
            pdfMerge.append(pdfReader)
            pdfFile.close()
    elif(len(Opt)==1):
        li=os.listdir(Opt[0])
        li.sort()
        for filename in li:
            if filename.endswith('.pdf'):
                pdfFile = open(f"{Opt[0]}\{filename}", 'rb')
                pdfReader = PdfReader(pdfFile)
                pdfMerge.append(pdfReader)
                pdfFile.close()
    pdfMerge.write(f'{outputpdf}.pdf')
    print("Process Completed.....")
except Exception as e:
    print(f"Please Enter The Correct Input\nerror : {e}")