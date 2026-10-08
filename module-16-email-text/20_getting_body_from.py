# Ch16 | 20/36 | Getting the Body from a Raw Message [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

message.text_part != None
# OUT:    True
message.text_part.get_payload().decode(message.text_part.charset)
# OUT:  'So long, and thanks for all the fish!\r\n\r\n-Al\r\n'
message.html_part != None
# OUT:    True
message.html_part.get_payload().decode(message.html_part.charset)
# OUT:    '<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-Al
# OUT:    <br></div>\r\n'
