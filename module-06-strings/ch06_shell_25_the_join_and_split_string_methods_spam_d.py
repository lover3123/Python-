"""Chapter 6: Manipulating Strings
Section: The join() and split() String Methods
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch6: strings, text editing
File: ch06_shell_25_the_join_and_split_string_methods_spam_d.py (25 of 46 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = '''Dear Alice,
# OUT: How have you been? I am fine.
# OUT: There is a container in the fridge
# OUT: that is labeled "Milk Experiment".

# OUT: Please do not drink it.
# OUT: Sincerely,
# OUT: Bob'''
spam.split('\n')
# OUT: ['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the
# OUT: fridge', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.',
# OUT: 'Sincerely,', 'Bob']
