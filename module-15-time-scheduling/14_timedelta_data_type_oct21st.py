# Ch15 | 14/37 | The timedelta Data Type [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
oct21st
# OUT:    datetime.datetime(2015, 10, 21, 16, 29)
oct21st - aboutThirtyYears
# OUT:    datetime.datetime(1985, 10, 28, 16, 29)
oct21st - (2 * aboutThirtyYears)
# OUT:    datetime.datetime(1955, 11, 5, 16, 29)
