"""Chapter 13: PDF and Word Documents
Section: Run Attributes
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter13
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch13: PyPDF2, python-docx
File: ch13_shell_16_run_attributes_doc_docx_document_demo_do.py (16 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

doc = docx.Document('demo.docx')
doc.paragraphs[0].text
# OUT: 'Document Title'
doc.paragraphs[0].style
# OUT: 'Title'
doc.paragraphs[0].style = 'Normal'
doc.paragraphs[1].text
# OUT: 'A plain paragraph with some bold and some italic'
(doc.paragraphs[1].runs[0].text, doc.paragraphs[1].runs[1].text, doc.
# OUT: paragraphs[1].runs[2].text, doc.paragraphs[1].runs[3].text)
# OUT: ('A plain paragraph with some ', 'bold', ' and some ', 'italic')
doc.paragraphs[1].runs[0].style = 'QuoteChar'
doc.paragraphs[1].runs[1].underline = True
doc.paragraphs[1].runs[3].underline = True
doc.save('restyled.docx')
