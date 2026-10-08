"""Chapter 7: Pattern Matching with Regular Expressions
Section: Matching Specific Repetitions with Curly Brackets
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_19_matching_specific_repetitions_with_curly.py (19 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()
# OUT: 'HaHaHa'

mo2 = haRegex.search('Ha')
mo2 == None
# OUT: True
