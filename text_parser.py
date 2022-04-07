import PyPDF2
 
#constant
DATA_DIR = "" 
OUT_DIR = ""
 
#create file object variable
pdffileobj=open('1.pdf','rb')
 
#create reader variable that will read the pdffileobj
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
 
#This will store the number of pages of this pdf file
x=pdfreader.numPages
 
#create a variable that will select the selected number of pages
pageobj=pdfreader.getPage(x+1)
 
#(x+1) because python indentation starts with 0.
#create text variable which will store all text datafrom pdf file
text=pageobj.extractText()

file1=open(OUT_DIR,"w")
file1.writelines(text)