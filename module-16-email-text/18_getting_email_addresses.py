# Ch16 | 18/36 | Getting Email Addresses from a Raw Message [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
