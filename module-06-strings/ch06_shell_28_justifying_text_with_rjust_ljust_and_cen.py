"""Chapter 6: Manipulating Strings
Section: Justifying Text with rjust(), ljust(), and center()
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch6: strings, text editing
File: ch06_shell_28_justifying_text_with_rjust_ljust_and_cen.py (28 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

'Hello'.center(20)
# OUT: '       Hello       '
'Hello'.center(20, '=')
# OUT: '=======Hello========'
