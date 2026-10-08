# Ch9 | 03/23 | Moving and Renaming Files and Folders [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter9

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import shutil
shutil.move('C:\\bacon.txt', 'C:\\eggs')
# OUT: 'C:\\eggs\\bacon.txt'
