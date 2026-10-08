"""Chapter 18: GUI Automation Keyboard Mouse
Section: Analyzing the Screenshot
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch18: pyautogui
File: ch18_shell_18_analyzing_the_screenshot_import_pyautogu.py (18 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import pyautogui
im = pyautogui.screenshot()
im.getpixel((50, 200))
# OUT:    (130, 135, 144)
pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
# OUT:    True
pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))
# OUT:    False
