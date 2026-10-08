# Ch16 | 32/36 | Sending Text Messages [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

message.sid
# OUT:    'SM09520de7639ba3af137c6fcb7c5f4b51'
updatedMessage = twilioCli.messages.get(message.sid)
updatedMessage.status
# OUT:    'delivered'
updatedMessage.date_sent
# OUT:    datetime.datetime(2015, 7, 8, 1, 36, 18)
