# Ch13 | 13/23 | Getting the Full Text from a .docx File [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter13

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
