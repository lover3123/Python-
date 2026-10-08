# Ch15 | 09/37 | The datetime Module [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import datetime
datetime.datetime.now()
# OUT:  datetime.datetime(2015, 2, 27, 11, 10, 49, 55, 53)
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
dt.year, dt.month, dt.day
# OUT:    (2015, 10, 21)
dt.hour, dt.minute, dt.second
# OUT:    (16, 29, 0)
