# Ch6 | 33/46 | Copying and Pasting Strings with the pyperclip Module [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter6

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()
# OUT: 'Hello world!'
