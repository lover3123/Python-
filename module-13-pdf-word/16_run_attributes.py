# Ch13 | 16/23 | Run Attributes [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter13

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
