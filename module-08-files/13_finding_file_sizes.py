# Ch8 | 13/40 | Finding File Sizes and Folder Contents [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

os.path.getsize('C:\\Windows\\System32\\calc.exe')
# OUT: 776192
os.listdir('C:\\Windows\\System32')
# OUT: ['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
# OUT: --snip--
# OUT: 'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']
