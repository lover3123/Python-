"""Chapter 18: GUI Automation Keyboard Mouse
Section: Image Recognition
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch18: pyautogui
File: ch18_shell_23_image_recognition_pyautogui_locateonscre.py (23 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

pyautogui.locateOnScreen('submit.png')
# OUT: (643, 745, 70, 29)
pyautogui.center((643, 745, 70, 29))
# OUT: (678, 759)
pyautogui.click((678, 759))
