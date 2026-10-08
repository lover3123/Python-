# Ch16 | 12/36 | Searching for Email [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import pprint
pprint.pprint(imapObj.list_folders())
# OUT: [(('\\HasNoChildren',), '/', 'Drafts'),
# OUT:  (('\\HasNoChildren',), '/', 'Filler'),
# OUT:  (('\\HasNoChildren',), '/', 'INBOX'),
# OUT:  (('\\HasNoChildren',), '/', 'Sent'),
# OUT: --snip-
# OUT:  (('\\HasNoChildren', '\\Flagged'), '/', '[Gmail]/Starred'),
# OUT:  (('\\HasNoChildren', '\\Trash'), '/', '[Gmail]/Trash')]
