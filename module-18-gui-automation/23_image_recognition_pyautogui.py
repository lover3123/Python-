# Ch18 | 23/36 | Image Recognition [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter18

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

pyautogui.locateOnScreen('submit.png')
# OUT: (643, 745, 70, 29)
pyautogui.center((643, 745, 70, 29))
# OUT: (678, 759)
pyautogui.click((678, 759))
