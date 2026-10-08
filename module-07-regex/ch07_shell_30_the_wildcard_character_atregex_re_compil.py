"""Chapter 7: Pattern Matching with Regular Expressions
Section: The Wildcard Character
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_30_the_wildcard_character_atregex_re_compil.py (30 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
# OUT: ['cat', 'hat', 'sat', 'lat', 'mat']
