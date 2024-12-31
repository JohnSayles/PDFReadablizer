'''
pypdf: https://pypdf.readthedocs.io/en/latest/index.html
fpdf: http://www.fpdf.org/
tqdm: https://tqdm.github.io/

All three libraries are third party, so you should pip install before using
this program!
'''
from pypdf import PdfReader
from fpdf import FPDF
from tqdm import tqdm

# Write the name of your pdf file here. Make sure to place your file in the same directory as PDFReader.py
pdf_file_name = ""

old_pdf_file = PdfReader(pdf_file_name + ".pdf")
new_pdf_file = FPDF()

# Sets the font as arial
# Makes all unicode characters recognizable
new_pdf_file.add_font('sysfont', '', "arial.ttf", uni=True)
new_pdf_file.set_font("sysfont",size = 12)

# extracts the text from each page, and appends itself to the new, more readble, pdf file
for p in tqdm(range(old_pdf_file.get_num_pages()), desc="Processing Pages"):
    page = old_pdf_file.pages[p]
    page_text = page.extract_text()
    new_pdf_file.add_page()
    new_pdf_file.multi_cell(200, 8, txt=page_text, align="J")
new_pdf_file.output(pdf_file_name + "Readable" + ".pdf")
    
    
    
    
    
