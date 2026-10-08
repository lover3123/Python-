# Ch15 | 04/37 | The time.sleep() Function [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import time
for i in range(3):
# OUT:          print('Tick')
# OUT:          time.sleep(1)
# OUT:          print('Tock')
# OUT:          time.sleep(1)
# OUT:    Tick
# OUT:    Tock
# OUT:    Tick
# OUT:    Tock
# OUT:    Tick
# OUT:    Tock
time.sleep(5)
