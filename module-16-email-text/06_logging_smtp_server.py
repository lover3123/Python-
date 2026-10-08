# Ch16 | 06/36 | Logging in to the SMTP Server [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

smtpObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')
# OUT: (235, b'2.7.0 Accepted')
