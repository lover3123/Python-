"""Chapter 13: PDF and Word Documents
Section: Writing Word Documents
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter13
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch13: PyPDF2, python-docx
File: ch13_shell_18_writing_word_documents_import_docx.py (18 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import docx
doc = docx.Document()
doc.add_paragraph('Hello world!')
# OUT: <docx.text.Paragraph object at 0x000000000366AD30>
paraObj1 = doc.add_paragraph('This is a second paragraph.')
paraObj2 = doc.add_paragraph('This is a yet another paragraph.')
paraObj1.add_run(' This text is being added to the second paragraph.')
# OUT: <docx.text.Run object at 0x0000000003A2C860>
doc.save('multipleParagraphs.docx')
