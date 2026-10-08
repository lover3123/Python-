"""Chapter 8: Reading and Writing Files
Section: Backslash on Windows and Forward Slash on OS X and Linux
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch8: files
File: ch08_shell_02_backslash_on_windows_and_forward_slash_o.py (2 of 40 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
# OUT:         print(os.path.join('C:\\Users\\asweigart', filename))
# OUT: C:\Users\asweigart\accounts.txt
# OUT: C:\Users\asweigart\details.csv
# OUT: C:\Users\asweigart\invite.docx
