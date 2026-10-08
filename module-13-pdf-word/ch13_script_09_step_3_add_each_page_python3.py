"""Chapter 13: PDF and Word Documents
Section: Step 3: Add Each Page
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter13
Type: book script/example
PPT map: Syllabus Ch13: PyPDF2, python-docx
File: ch13_script_09_step_3_add_each_page_python3.py (9 of 23 in this chapter)
"""

   #! python3
   # combinePdfs.py - Combines all the PDFs in the current working directory into
   # a single PDF.

   import PyPDF2, os

   --snip--

   # Loop through all the PDF files.
   for filename in pdfFiles:
   --snip--
       # Loop through all the pages (except the first) and add them.
     for pageNum in range(1, pdfReader.numPages):
           pageObj = pdfReader.getPage(pageNum)
           pdfWriter.addPage(pageObj)

   # TODO: Save the resulting PDF to a file.
