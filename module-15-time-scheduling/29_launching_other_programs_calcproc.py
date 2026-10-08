# Ch15 | 29/37 | Launching Other Programs from Python [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
calcProc.poll() == None
# OUT:    True
calcProc.wait()
# OUT:    0
calcProc.poll()
# OUT:    0
