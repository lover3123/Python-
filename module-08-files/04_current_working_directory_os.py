# Ch8 | 04/40 | The Current Working Directory [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

os.chdir('C:\\ThisFolderDoesNotExist')
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#18>", line 1, in <module>
# OUT:     os.chdir('C:\\ThisFolderDoesNotExist')
# OUT: FileNotFoundError: [WinError 2] The system cannot find the file specified:
# OUT: 'C:\\ThisFolderDoesNotExist'
