"""Chapter 7: Pattern Matching with Regular Expressions
Section: Grouping with Parentheses
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_09_grouping_with_parentheses_mo_groups.py (9 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

mo.groups()
# OUT: ('415', '555-4242')
areaCode, mainNumber = mo.groups()
print(areaCode)
# OUT: 415
print(mainNumber)
# OUT: 555-4242
