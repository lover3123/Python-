# Ch16 | 04/36 | Sending the SMTP “Hello” Message [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

smtpObj.ehlo()
# OUT: (250, b'mx.google.com at your service, [216.172.148.131]\nSIZE 35882577\
# OUT: n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
