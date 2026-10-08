"""Chapter 7: Pattern Matching with Regular Expressions
Section: Substituting Strings with the sub() Method
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_37_substituting_strings_with_the_sub_method.py (37 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent
# OUT: Eve knew Agent Bob was a double agent.')
# OUT: A**** told C**** that E**** knew B**** was a double agent.'
