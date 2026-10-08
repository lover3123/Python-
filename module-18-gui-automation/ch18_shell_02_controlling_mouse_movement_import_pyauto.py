"""Chapter 18: GUI Automation Keyboard Mouse
Section: Controlling Mouse Movement
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch18: pyautogui
File: ch18_shell_02_controlling_mouse_movement_import_pyauto.py (2 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import pyautogui
pyautogui.size()
# OUT: (1920, 1080)
width, height = pyautogui.size()
