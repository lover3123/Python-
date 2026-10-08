"""Chapter 8: Reading and Writing Files
Section: Checking Path Validity
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch8: files
File: ch08_shell_15_checking_path_validity_os_path_exists_c_.py (15 of 40 in this chapter)
"""

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
