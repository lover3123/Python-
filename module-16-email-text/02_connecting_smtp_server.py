# Ch16 | 02/36 | Connecting to an SMTP Server [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
type(smtpObj)
# OUT: <class 'smtplib.SMTP'>
