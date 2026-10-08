# Ch15 | 11/37 | The datetime Module [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
halloween2015 == oct31_2015
# OUT:    True
halloween2015 > newyears2016
# OUT:    False
newyears2016 > halloween2015
# OUT:    True
newyears2016 != oct31_2015
# OUT:    True
