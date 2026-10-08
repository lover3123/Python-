# Ch16 | 10/36 | Connecting to an IMAP Server [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
