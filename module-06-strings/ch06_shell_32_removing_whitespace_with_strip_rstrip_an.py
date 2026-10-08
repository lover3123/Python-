"""Chapter 6: Manipulating Strings
Section: Removing Whitespace with strip(), rstrip(), and lstrip()
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch6: strings, text editing
File: ch06_shell_32_removing_whitespace_with_strip_rstrip_an.py (32 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
# OUT: 'BaconSpamEggs'
