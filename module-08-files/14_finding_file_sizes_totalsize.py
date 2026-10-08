# Ch8 | 14/40 | Finding File Sizes and Folder Contents [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
# OUT:       totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(totalSize)
# OUT: 1117846456
