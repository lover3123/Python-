"""Chapter 18: GUI Automation Keyboard Mouse
Section: Step 3: Start Typing Data
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch18: pyautogui
File: ch18_shell_33_step_3_start_typing_data_python3.py (33 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

# OUT:    #! python3
# OUT:    # formFiller.py - Automatically fills in the form.

# OUT:    --snip--

# OUT:    for person in formData:
# OUT:        # Give the user a chance to kill the script.
# OUT:        print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
# OUT:      time.sleep(5)

# OUT:        # Wait until the form page has loaded.
# OUT:      while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1],
# OUT:        submitButtonColor):
# OUT:            time.sleep(0.5)

# OUT:    --snip--
