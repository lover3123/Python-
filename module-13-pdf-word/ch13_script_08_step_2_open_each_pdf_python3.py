"""Chapter 13: PDF and Word Documents
Section: Step 2: Open Each PDF
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter13
Type: book script/example
PPT map: Syllabus Ch13: PyPDF2, python-docx
File: ch13_script_08_step_2_open_each_pdf_python3.py (8 of 23 in this chapter)
"""

#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# a single PDF.

import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
--snip--
# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # TODO: Loop through all the pages (except the first) and add them.

# TODO: Save the resulting PDF to a file.
