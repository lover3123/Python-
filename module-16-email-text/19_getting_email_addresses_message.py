# Ch16 | 19/36 | Getting Email Addresses from a Raw Message [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

message.get_subject()
# OUT: 'Hello!'
message.get_addresses('from')
# OUT: [('Edward Snowden', 'esnowden@nsa.gov')]
message.get_addresses('to')
# OUT: [(Jane Doe', 'my_email_address@gmail.com')]
message.get_addresses('cc')
# OUT: []
message.get_addresses('bcc')
# OUT: []
