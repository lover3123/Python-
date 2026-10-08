# Ch15 | 06/37 | Rounding Numbers [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import time
now = time.time()
now
# OUT: 1425064108.017826
round(now, 2)
# OUT: 1425064108.02
round(now, 4)
# OUT: 1425064108.0178
round(now)
# OUT: 1425064108
