"""Chapter 7: Pattern Matching with Regular Expressions
Section: Case-Insensitive Matching
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_35_case_insensitive_matching_robocop_re_com.py (35 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

robocop = re.compile(r'robocop', re.I)
robocop.search('Robocop is part man, part machine, all cop.').group()
# OUT: 'Robocop'

robocop.search('ROBOCOP protects the innocent.').group()
# OUT: 'ROBOCOP'

robocop.search('Al, why does your programming book talk about robocop so much?').group()
# OUT: 'robocop'
