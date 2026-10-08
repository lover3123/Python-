"""Chapter 5: Dictionaries and Structuring Data
Section: Dictionaries vs. Lists
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter5
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch5: dicts, structuring data
File: ch05_shell_04_dictionaries_vs_lists_spam_name_zophie_a.py (4 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = {'name': 'Zophie', 'age': 7}
spam['color']
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#1>", line 1, in <module>
# OUT:     spam['color']
# OUT: KeyError: 'color'
