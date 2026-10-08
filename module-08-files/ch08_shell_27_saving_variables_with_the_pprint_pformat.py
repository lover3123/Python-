"""Chapter 8: Reading and Writing Files
Section: Saving Variables with the pprint.pformat() Function
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch8: files
File: ch08_shell_27_saving_variables_with_the_pprint_pformat.py (27 of 40 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import myCats
myCats.cats
# OUT: [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
myCats.cats[0]
# OUT: {'name': 'Zophie', 'desc': 'chubby'}
myCats.cats[0]['name']
# OUT: 'Zophie'
