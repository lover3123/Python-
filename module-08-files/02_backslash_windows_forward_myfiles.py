# Ch8 | 02/40 | Backslash on Windows and Forward Slash on OS X and Linux [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
# OUT:         print(os.path.join('C:\\Users\\asweigart', filename))
# OUT: C:\Users\asweigart\accounts.txt
# OUT: C:\Users\asweigart\details.csv
# OUT: C:\Users\asweigart\invite.docx
