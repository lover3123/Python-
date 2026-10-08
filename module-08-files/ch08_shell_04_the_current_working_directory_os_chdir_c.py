"""Chapter 8: Reading and Writing Files
Section: The Current Working Directory
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch8: files
File: ch08_shell_04_the_current_working_directory_os_chdir_c.py (4 of 40 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

os.chdir('C:\\ThisFolderDoesNotExist')
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#18>", line 1, in <module>
# OUT:     os.chdir('C:\\ThisFolderDoesNotExist')
# OUT: FileNotFoundError: [WinError 2] The system cannot find the file specified:
# OUT: 'C:\\ThisFolderDoesNotExist'
