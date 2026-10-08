"""Chapter 13: PDF and Word Documents
Section: Creating PDFs
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter13
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch13: PyPDF2, python-docx
File: ch13_shell_04_creating_pdfs_import_pypdf2.py (4 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)
# OUT:    {'/Contents': [IndirectObject(961, 0), IndirectObject(962, 0),
# OUT:    --snip--
# OUT:    }
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()
