# Ch13 | 07/23 | Step 1: Find All PDF Files [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter13

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
