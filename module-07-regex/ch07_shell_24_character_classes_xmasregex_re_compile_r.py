"""Chapter 7: Pattern Matching with Regular Expressions
Section: Character Classes
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_24_character_classes_xmasregex_re_compile_r.py (24 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7
# OUT: swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# OUT: ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6
# OUT: geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
