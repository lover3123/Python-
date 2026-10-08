# Ch8 | 07/40 | Handling Absolute and Relative Paths [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

os.path.relpath('C:\\Windows', 'C:\\')
# OUT: 'Windows'
os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
# OUT: '..\\..\\Windows'
os.getcwd() 'C:\\Python34'
