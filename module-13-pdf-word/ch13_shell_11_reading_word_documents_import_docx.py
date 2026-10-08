"""Chapter 13: PDF and Word Documents
Section: Reading Word Documents
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter13
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch13: PyPDF2, python-docx
File: ch13_shell_11_reading_word_documents_import_docx.py (11 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import docx
doc = docx.Document('demo.docx')
len(doc.paragraphs)
# OUT:    7
doc.paragraphs[0].text
# OUT:    'Document Title'
doc.paragraphs[1].text
# OUT:    'A plain paragraph with some bold and some italic'
len(doc.paragraphs[1].runs)
# OUT:    4
doc.paragraphs[1].runs[0].text
# OUT:    'A plain paragraph with some '
doc.paragraphs[1].runs[1].text
# OUT:    'bold'
doc.paragraphs[1].runs[2].text
# OUT:    ' and some '
# OUT: ➒ >>> doc.paragraphs[1].runs[3].text
# OUT:    'italic'
