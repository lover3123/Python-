"""Chapter 5: Dictionaries and Structuring Data
Section: The get() Method
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter5
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch5: dicts, structuring data
File: ch05_shell_13_the_get_method_picnicitems_apples_5_cups.py (13 of 37 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#34>", line 1, in <module>
# OUT:     'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
# OUT: KeyError: 'eggs'
