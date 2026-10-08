"""Chapter 7: Pattern Matching with Regular Expressions
Section: The Caret and Dollar Sign Characters
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_29_the_caret_and_dollar_sign_characters_who.py (29 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
# OUT: <_sre.SRE_Match object; span=(0, 10), match='1234567890'>
wholeStringIsNum.search('12345xyz67890') == None
# OUT: True
wholeStringIsNum.search('12 34567890') == None
# OUT: True
