# Ch16 | 21/36 | Deleting Emails [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

imapObj.select_folder('INBOX', readonly=False)
UIDs = imapObj.search(['ON 09-Jul-2015'])
UIDs
# OUT:    [40066]
imapObj.delete_messages(UIDs)
# OUT:  {40066: ('\\Seen', '\\Deleted')}
imapObj.expunge()
# OUT:    ('Success', [(5452, 'EXISTS')])
