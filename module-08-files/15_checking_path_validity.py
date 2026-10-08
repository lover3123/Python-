# Ch8 | 15/40 | Checking Path Validity [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

os.path.exists('C:\\Windows')
# OUT: True
os.path.exists('C:\\some_made_up_folder')
# OUT: False
os.path.isdir('C:\\Windows\\System32')
# OUT: True
os.path.isfile('C:\\Windows\\System32')
# OUT: False
os.path.isdir('C:\\Windows\\System32\\calc.exe')
# OUT: False
os.path.isfile('C:\\Windows\\System32\\calc.exe')
# OUT: True
