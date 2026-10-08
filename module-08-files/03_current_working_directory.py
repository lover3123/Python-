# Ch8 | 03/40 | The Current Working Directory [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import os
os.getcwd()
# OUT: 'C:\\Python34'
os.chdir('C:\\Windows\\System32')
os.getcwd()
# OUT: 'C:\\Windows\\System32'
