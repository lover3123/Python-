"""Chapter 5: Dictionaries and Structuring Data
Section: The setdefault() Method
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter5
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch5: dicts, structuring data
File: ch05_shell_15_the_setdefault_method_spam_name_pooka_ag.py (15 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
# OUT: 'black'
spam
# OUT: {'color': 'black', 'age': 5, 'name': 'Pooka'}
spam.setdefault('color', 'white')
# OUT: 'black'
spam
# OUT: {'color': 'black', 'age': 5, 'name': 'Pooka'}
