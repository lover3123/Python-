# Ch18 | 33/36 | Step 3: Start Typing Data [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter18

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
