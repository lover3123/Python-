"""Chapter 7: Pattern Matching with Regular Expressions
Section: Optional Matching with the Question Mark
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_14_optional_matching_with_the_question_mark.py (14 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()
# OUT: '415-555-4242'

mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()
# OUT: '555-4242'
