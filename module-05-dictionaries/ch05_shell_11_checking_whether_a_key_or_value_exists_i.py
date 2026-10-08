"""Chapter 5: Dictionaries and Structuring Data
Section: Checking Whether a Key or Value Exists in a Dictionary
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter5
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch5: dicts, structuring data
File: ch05_shell_11_checking_whether_a_key_or_value_exists_i.py (11 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys()
# OUT: True
'Zophie' in spam.values()
# OUT: True
'color' in spam.keys()
# OUT: False
'color' not in spam.keys()
# OUT: True
'color' in spam
# OUT: False
