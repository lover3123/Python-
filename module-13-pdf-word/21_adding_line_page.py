# Ch13 | 21/23 | Adding Line and Page Breaks [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter13

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

doc = docx.Document()
doc.add_paragraph('This is on the first page!')
# OUT:    <docx.text.Paragraph object at 0x0000000003785518>
doc.paragraphs[0].runs[0].add_break(docx.text.WD_BREAK.PAGE)
doc.add_paragraph('This is on the second page!')
# OUT:    <docx.text.Paragraph object at 0x00000000037855F8>
doc.save('twoPage.docx')
