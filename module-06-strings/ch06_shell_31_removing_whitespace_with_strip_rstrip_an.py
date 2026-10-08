"""Chapter 6: Manipulating Strings
Section: Removing Whitespace with strip(), rstrip(), and lstrip()
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch6: strings, text editing
File: ch06_shell_31_removing_whitespace_with_strip_rstrip_an.py (31 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = '    Hello World     '
spam.strip()
# OUT: 'Hello World'
spam.lstrip()
# OUT: 'Hello World '
spam.rstrip()
# OUT: '    Hello World'
