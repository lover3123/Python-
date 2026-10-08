"""Chapter 13: PDF and Word Documents
Section: Adding Pictures
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter13
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch13: PyPDF2, python-docx
File: ch13_shell_22_adding_pictures_doc_add_picture_zophie_p.py (22 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

doc.add_picture('zophie.png', width=docx.shared.Inches(1),
# OUT: height=docx.shared.Cm(4))
# OUT: <docx.shape.InlineShape object at 0x00000000036C7D30>
