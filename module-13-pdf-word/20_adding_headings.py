# Ch13 | 20/23 | Adding Headings [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter13

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
