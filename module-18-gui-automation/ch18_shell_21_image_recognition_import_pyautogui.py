"""Chapter 18: GUI Automation Keyboard Mouse
Section: Image Recognition
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch18: pyautogui
File: ch18_shell_21_image_recognition_import_pyautogui.py (21 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import pyautogui
pyautogui.locateOnScreen('submit.png')
# OUT: (643, 745, 70, 29)
