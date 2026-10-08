"""Chapter 6: Manipulating Strings
Section: Indexing and Slicing Strings
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch6: strings, text editing
File: ch06_shell_10_indexing_and_slicing_strings_spam_hello_.py (10 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = 'Hello world!'
spam[0]
# OUT: 'H'
spam[4]
# OUT: 'o'
spam[-1]
# OUT: '!'
spam[0:5]
# OUT: 'Hello'
spam[:5]
# OUT: 'Hello'
spam[6:]
# OUT: 'world!'
