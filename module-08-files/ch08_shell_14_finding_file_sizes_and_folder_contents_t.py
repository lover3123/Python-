"""Chapter 8: Reading and Writing Files
Section: Finding File Sizes and Folder Contents
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch8: files
File: ch08_shell_14_finding_file_sizes_and_folder_contents_t.py (14 of 40 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
# OUT:       totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(totalSize)
# OUT: 1117846456
