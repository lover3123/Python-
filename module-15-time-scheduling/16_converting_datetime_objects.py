# Ch15 | 16/37 | Converting datetime Objects into Strings [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
# OUT: '2015/10/21 16:29:00'
oct21st.strftime('%I:%M %p')
# OUT: '04:29 PM'
oct21st.strftime("%B of '%y")
# OUT: "October of '15"
