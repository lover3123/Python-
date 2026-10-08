"""Chapter 7: Pattern Matching with Regular Expressions
Section: Matching Multiple Groups with the Pipe
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_11_matching_multiple_groups_with_the_pipe_h.py (11 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()
# OUT: 'Batman'

mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()
# OUT: 'Tina Fey'
