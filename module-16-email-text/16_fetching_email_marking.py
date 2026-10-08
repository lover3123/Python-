# Ch16 | 16/36 | Fetching an Email and Marking It As Read [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
import pprint
pprint.pprint(rawMessages)
# OUT: {40040: {'BODY[]': 'Delivered-To: my_email_address@gmail.com\r\n'
# OUT:                    'Received: by 10.76.71.167 with SMTP id '
# OUT: --snip--
# OUT:                    '\r\n'
# OUT:                    '------=_Part_6000970_707736290.1404819487066--\r\n',
# OUT:          'SEQ': 5430}}
