# Ch13 | 02/23 | Decrypting PDFs [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter13

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
