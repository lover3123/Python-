# Ch6 | 31/46 | Removing Whitespace with strip(), rstrip(), and lstrip() [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter6

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

spam = '    Hello World     '
spam.strip()
# OUT: 'Hello World'
spam.lstrip()
# OUT: 'Hello World '
spam.rstrip()
# OUT: '    Hello World'
