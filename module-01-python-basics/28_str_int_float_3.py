# Ch1 | 28/30 | The str(), int(), and float() Functions [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter1

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

int('99.99')
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#18>", line 1, in <module>
# OUT:     int('99.99')
# OUT: ValueError: invalid literal for int() with base 10: '99.99'
int('twelve')
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#19>", line 1, in <module>
# OUT:     int('twelve')
# OUT: ValueError: invalid literal for int() with base 10: 'twelve'
