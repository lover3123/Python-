# Ch16 | 03/36 | Connecting to an SMTP Server [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
