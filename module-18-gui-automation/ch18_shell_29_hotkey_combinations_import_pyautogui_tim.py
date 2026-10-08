"""Chapter 18: GUI Automation Keyboard Mouse
Section: Hotkey Combinations
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch18: pyautogui
File: ch18_shell_29_hotkey_combinations_import_pyautogui_tim.py (29 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import pyautogui, time
def commentAfterDelay():
# OUT:        pyautogui.click(100, 100)
# OUT:        pyautogui.typewrite('In IDLE, Alt-3 comments out a line.')
# OUT:          time.sleep(2)
# OUT:        pyautogui.hotkey('alt', '3')

commentAfterDelay()
