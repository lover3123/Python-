"""Chapter 18: GUI Automation Keyboard Mouse
Section: Sending a String from the Keyboard
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch18: pyautogui
File: ch18_shell_24_sending_a_string_from_the_keyboard_pyaut.py (24 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

pyautogui.click(100, 100); pyautogui.typewrite('Hello world!')
