"""Chapter 13: PDF and Word Documents
Section: Decrypting PDFs
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter13
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch13: PyPDF2, python-docx
File: ch13_shell_02_decrypting_pdfs_import_pypdf2.py (2 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted
# OUT:    True
pdfReader.getPage(0)
# OUT:  Traceback (most recent call last):
# OUT:      File "<pyshell#173>", line 1, in <module>
# OUT:        pdfReader.getPage()
# OUT:      --snip--
# OUT:      File "C:\Python34\lib\site-packages\PyPDF2\pdf.py", line 1173, in getObject
# OUT:        raise utils.PdfReadError("file has not been decrypted")
# OUT:    PyPDF2.utils.PdfReadError: file has not been decrypted
pdfReader.decrypt('rosebud')
# OUT:    1
pageObj = pdfReader.getPage(0)
