"""Chapter 7: Pattern Matching with Regular Expressions
Section: Matching One or More with the Plus
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_16_matching_one_or_more_with_the_plus_batre.py (16 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()
# OUT: 'Batwoman'

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
# OUT: 'Batwowowowoman'

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
# OUT: True
