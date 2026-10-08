"""Chapter 9: Organizing Files
Section: Moving and Renaming Files and Folders
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter9
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch9: shutil, os, zip
File: ch09_shell_06_moving_and_renaming_files_and_folders_sh.py (6 of 23 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')
# OUT: Traceback (most recent call last):
# OUT:   File "C:\Python34\lib\shutil.py", line 521, in move
# OUT:     os.rename(src, real_dst)
# OUT: FileNotFoundError: [WinError 3] The system cannot find the path specified:
# OUT: 'spam.txt' -> 'c:\\does_not_exist\\eggs\\ham'

# OUT: During handling of the above exception, another exception occurred:

# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#29>", line 1, in <module>
# OUT:     shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')
# OUT:   File "C:\Python34\lib\shutil.py", line 533, in move
# OUT:     copy2(src, real_dst)
# OUT:   File "C:\Python34\lib\shutil.py", line 244, in copy2
# OUT:     copyfile(src, dst, follow_symlinks=follow_symlinks)
# OUT:   File "C:\Python34\lib\shutil.py", line 108, in copyfile
# OUT:     with open(dst, 'wb') as fdst:
# OUT: FileNotFoundError: [Errno 2] No such file or directory: 'c:\\does_not_exist\\
# OUT: eggs\\ham'
