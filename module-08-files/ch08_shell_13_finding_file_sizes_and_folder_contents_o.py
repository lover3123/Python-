"""Chapter 8: Reading and Writing Files
Section: Finding File Sizes and Folder Contents
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch8: files
File: ch08_shell_13_finding_file_sizes_and_folder_contents_o.py (13 of 40 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

os.path.getsize('C:\\Windows\\System32\\calc.exe')
# OUT: 776192
os.listdir('C:\\Windows\\System32')
# OUT: ['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
# OUT: --snip--
# OUT: 'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']
