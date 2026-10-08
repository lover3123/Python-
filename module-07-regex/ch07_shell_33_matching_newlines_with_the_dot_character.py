"""Chapter 7: Pattern Matching with Regular Expressions
Section: Matching Newlines with the Dot Character
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_33_matching_newlines_with_the_dot_character.py (33 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.
# OUT: \nUphold the law.').group()
# OUT: 'Serve the public trust.'

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.
# OUT: \nUphold the law.').group()
# OUT: 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
