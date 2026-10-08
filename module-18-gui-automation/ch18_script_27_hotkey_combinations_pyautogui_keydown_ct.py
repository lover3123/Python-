"""Chapter 18: GUI Automation Keyboard Mouse
Section: Hotkey Combinations
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: book script/example
PPT map: Syllabus Ch18: pyautogui
File: ch18_script_27_hotkey_combinations_pyautogui_keydown_ct.py (27 of 36 in this chapter)
"""

pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')
