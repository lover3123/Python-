"""Chapter 8: Reading and Writing Files
Section: Handling Absolute and Relative Paths
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch8: files
File: ch08_shell_08_handling_absolute_and_relative_paths_pat.py (8 of 40 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path)
# OUT: 'calc.exe'
os.path.dirname(path)
# OUT: 'C:\\Windows\\System32'
