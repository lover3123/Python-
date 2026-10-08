"""Chapter 18: GUI Automation Keyboard Mouse
Section: Scrolling the Mouse
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch18: pyautogui
File: ch18_shell_14_scrolling_the_mouse_import_pyperclip.py (14 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import pyperclip
numbers = ''
for i in range(200):
# OUT:       numbers = numbers + str(i) + '\n'

pyperclip.copy(numbers)
