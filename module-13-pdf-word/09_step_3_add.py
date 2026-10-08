# Ch13 | 09/23 | Step 3: Add Each Page [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter13

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
