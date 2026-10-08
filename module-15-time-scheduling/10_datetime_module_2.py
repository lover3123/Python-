# Ch15 | 10/37 | The datetime Module [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

datetime.datetime.fromtimestamp(1000000)
# OUT: datetime.datetime(1970, 1, 12, 5, 46, 40)
datetime.datetime.fromtimestamp(time.time())
# OUT: datetime.datetime(2015, 2, 27, 11, 13, 0, 604980)
