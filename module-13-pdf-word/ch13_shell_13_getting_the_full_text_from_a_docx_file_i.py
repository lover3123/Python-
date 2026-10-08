"""Chapter 13: PDF and Word Documents
Section: Getting the Full Text from a .docx File
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter13
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch13: PyPDF2, python-docx
File: ch13_shell_13_getting_the_full_text_from_a_docx_file_i.py (13 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import readDocx
print(readDocx.getText('demo.docx'))
# OUT: Document Title
# OUT: A plain paragraph with some bold and some italic
# OUT: Heading, level 1
# OUT: Intense quote
# OUT: first item in unordered list
# OUT: first item in ordered list
