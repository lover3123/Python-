"""Chapter 13: PDF and Word Documents
Section: Step 1: Find All PDF Files
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter13
Type: book script/example
PPT map: Syllabus Ch13: PyPDF2, python-docx
File: ch13_script_07_step_1_find_all_pdf_files_python3.py (7 of 23 in this chapter)
"""

   #! python3
   # combinePdfs.py - Combines all the PDFs in the current working directory into
   # into a single PDF.

 import PyPDF2, os

   # Get all the PDF filenames.
   pdfFiles = []
   for filename in os.listdir('.'):
       if filename.endswith('.pdf'):
         pdfFiles.append(filename)
 pdfFiles.sort(key=str.lower)

 pdfWriter = PyPDF2.PdfFileWriter()

   # TODO: Loop through all the PDF files.

   # TODO: Loop through all the pages (except the first) and add them.

   # TODO: Save the resulting PDF to a file.
