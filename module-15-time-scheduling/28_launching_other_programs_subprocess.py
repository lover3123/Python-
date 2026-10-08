# Ch15 | 28/37 | Launching Other Programs from Python [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import subprocess
subprocess.Popen('/usr/bin/gnome-calculator')
# OUT: <subprocess.Popen object at 0x7f2bcf93b20>
