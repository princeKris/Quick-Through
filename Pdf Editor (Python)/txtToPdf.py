from fpdf import FPDF
print("\n\n")
print(" TXT To PDF ".center(40,"+"))
pdf = FPDF()
pdf.add_page()
pdf.set_font('Times','',14)
with open(str(input("Enter The Text File Path : ")),"r") as ou:
    pdf.multi_cell(0, 10,txt=ou.read(),border=0,align='L')
pdf.output(str(input("Enter The Output PDF File Name : ")), 'F')