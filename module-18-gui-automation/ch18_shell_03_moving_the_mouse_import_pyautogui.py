"""Chapter 18: GUI Automation Keyboard Mouse
Section: Moving the Mouse
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch18: pyautogui
File: ch18_shell_03_moving_the_mouse_import_pyautogui.py (3 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import pyautogui
for i in range(10):
# OUT:       pyautogui.moveTo(100, 100, duration=0.25)
# OUT:       pyautogui.moveTo(200, 100, duration=0.25)
# OUT:       pyautogui.moveTo(200, 200, duration=0.25)
# OUT:       pyautogui.moveTo(100, 200, duration=0.25)
