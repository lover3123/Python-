# Ch16 | 14/36 | Searching for Email [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

UIDs = imapObj.search(['SINCE 05-Jul-2015'])
UIDs
# OUT: [40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
