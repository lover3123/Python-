"""Chapter 13: PDF and Word Documents
Section: Adding Headings
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter13
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch13: PyPDF2, python-docx
File: ch13_shell_20_adding_headings_doc_docx_document.py (20 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

doc = docx.Document()
doc.add_heading('Header 0', 0)
# OUT: <docx.text.Paragraph object at 0x00000000036CB3C8>
doc.add_heading('Header 1', 1)
# OUT: <docx.text.Paragraph object at 0x00000000036CB630>
doc.add_heading('Header 2', 2)
# OUT: <docx.text.Paragraph object at 0x00000000036CB828>
doc.add_heading('Header 3', 3)
# OUT: <docx.text.Paragraph object at 0x00000000036CB2E8>
doc.add_heading('Header 4', 4)
# OUT: <docx.text.Paragraph object at 0x00000000036CB3C8>
doc.save('headings.docx')
