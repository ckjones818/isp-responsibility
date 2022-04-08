from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
from docx import Document
import io
import os
import re
 
# constant
PDF_DATA_DIR = "./data/pdf/"
DOC_DATA_DIR = "./data/doc/"
OUT_DIR = "./data/text/"

# parse pdf first
for pdf in os.listdir(PDF_DATA_DIR):
    # initialize PDF parser
    resource_manager = PDFResourceManager()
    file_handler = io.StringIO()
    converter = TextConverter(resource_manager, file_handler, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    
    # open pdf to get text
    in_path = os.path.join(PDF_DATA_DIR, pdf)
    with open(in_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=False):
            page_interpreter.process_page(page)

        text = file_handler.getvalue()
        fh.close()
    
    # write text to file
    file_name = pdf.replace(".pdf", ".txt")
    out_path = os.path.join(OUT_DIR, file_name)
    file1=open(out_path,"w")
    file1.writelines(text)
    file1.close()

    # close open handles
    converter.close()
    file_handler.close()
    
# parse the docx
for docs in os.listdir(DOC_DATA_DIR):
    # initialize docx parser
    try:
        doc = Document(os.path.join(DOC_DATA_DIR, docs))
        text = []
        [text.append(para.text) for para in doc.paragraphs]
        text = '\n'.join(text)
        
        # write text to file
        file_name = re.sub('.docx?', '.txt', docs)
        out_path = os.path.join(OUT_DIR, file_name)
        file1=open(out_path,"w")
        file1.writelines(text)
        file1.close()
    except Exception as e:
        print(e)
