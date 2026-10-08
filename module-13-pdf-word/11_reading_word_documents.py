# Ch13 | 11/23 | Reading Word Documents [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter13

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
