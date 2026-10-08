"""Chapter 7: Pattern Matching with Regular Expressions
Section: Optional Matching with the Question Mark
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_13_optional_matching_with_the_question_mark.py (13 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
# OUT: 'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
# OUT: 'Batwoman'
