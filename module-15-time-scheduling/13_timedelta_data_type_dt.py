# Ch15 | 13/37 | The timedelta Data Type [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

dt = datetime.datetime.now()
dt
# OUT: datetime.datetime(2015, 2, 27, 18, 38, 50, 636181)
thousandDays = datetime.timedelta(days=1000)
dt + thousandDays
# OUT: datetime.datetime(2017, 11, 23, 18, 38, 50, 636181)
