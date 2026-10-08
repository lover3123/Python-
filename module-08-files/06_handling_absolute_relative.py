# Ch8 | 06/40 | Handling Absolute and Relative Paths [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

os.path.abspath('.')
# OUT: 'C:\\Python34'
os.path.abspath('.\\Scripts')
# OUT: 'C:\\Python34\\Scripts'
os.path.isabs('.')
# OUT: False
os.path.isabs(os.path.abspath('.'))
# OUT: True
