"""Chapter 7: Pattern Matching with Regular Expressions
Section: The Caret and Dollar Sign Characters
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch7: regex
File: ch07_shell_28_the_caret_and_dollar_sign_characters_end.py (28 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
# OUT: <_sre.SRE_Match object; span=(16, 17), match='2'>
endsWithNumber.search('Your number is forty two.') == None
# OUT: True
