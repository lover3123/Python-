"""Chapter 10: Debugging
Section: Getting the Traceback as a String
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter10
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch10: raise, assert, logging, debugger
File: ch10_shell_06_getting_the_traceback_as_a_string_import.py (6 of 24 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import traceback
try:
# OUT:          raise Exception('This is the error message.')
# OUT: except:
# OUT:          errorFile = open('errorInfo.txt', 'w')
# OUT:          errorFile.write(traceback.format_exc())
# OUT:          errorFile.close()
# OUT:          print('The traceback info was written to errorInfo.txt.')

# OUT: 116
# OUT: The traceback info was written to errorInfo.txt.
