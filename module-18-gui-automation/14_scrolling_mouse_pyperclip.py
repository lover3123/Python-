# Ch18 | 14/36 | Scrolling the Mouse [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter18

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import pyperclip
numbers = ''
for i in range(200):
# OUT:       numbers = numbers + str(i) + '\n'

pyperclip.copy(numbers)
