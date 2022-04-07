import PyPDF2
 
#constant
DATA_DIR = "./data/pdf/"
FILE = "Absaraka_Cooperative_Telephone_Co._Inc..pdf" 
OUT_DIR = "./data/text/"
 
#create file object variable
pdffileobj=open(DATA_DIR + FILE,'rb')
 
#create reader variable that will read the pdffileobj
pdfreader=PyPDF2.PdfFileReader(pdffileobj, strict=False)
print()
 
#This will store the number of pages of this pdf file
x=pdfreader.numPages
 
#create a variable that will select the selected number of pages
pageobj=pdfreader.getPage(x+1)
 
#(x+1) because python indentation starts with 0.
#create text variable which will store all text datafrom pdf file
text=pageobj.extractText()

file_name = FILE.replace(".pdf", ".txt")

file1=open(OUT_DIR + file_name,"w")
file1.writelines(text)