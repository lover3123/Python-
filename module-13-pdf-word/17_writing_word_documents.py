# Ch13 | 17/23 | Writing Word Documents [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter13

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import docx
doc = docx.Document()
doc.add_paragraph('Hello world!')
# OUT: <docx.text.Paragraph object at 0x0000000003B56F60>
doc.save('helloworld.docx')
