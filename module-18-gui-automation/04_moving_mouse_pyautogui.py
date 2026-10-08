# Ch18 | 04/36 | Moving the Mouse [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter18

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import pyautogui
for i in range(10):
# OUT:       pyautogui.moveRel(100, 0, duration=0.25)
# OUT:       pyautogui.moveRel(0, 100, duration=0.25)
# OUT:       pyautogui.moveRel(-100, 0, duration=0.25)
# OUT:       pyautogui.moveRel(0, -100, duration=0.25)
