# Ch15 | 12/37 | The timedelta Data Type [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
# OUT:    (11, 36548, 0)
delta.total_seconds()
# OUT:    986948.0
str(delta)
# OUT:    '11 days, 10:09:08'
