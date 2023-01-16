import PyPDF2 as pdf
from PyPDF2 import PdfReader
pdf_document = "C:/Users/vpesp/VC projects/PythonCourse/example2.pdf"  
i=0
with open(pdf_document, "rb") as pdffile:
    pdf = PdfReader(pdffile)
    pages=len(pdf.pages)
    with open('output.txt', "w+",encoding='utf-8') as file: 
        for i in range(pages):
            file.write(pdf.pages[i].extract_text())
with open('output.txt','r',encoding='utf-8') as file:
    text=file.read()



