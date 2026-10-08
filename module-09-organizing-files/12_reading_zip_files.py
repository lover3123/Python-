# Ch9 | 12/23 | Reading ZIP Files [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter9

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import zipfile, os
os.chdir('C:\\')    # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
# OUT:    ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
# OUT:    13908
spamInfo.compress_size
# OUT:    3828
'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
# OUT:    .compress_size, 2))
# OUT:    'Compressed file is 3.63x smaller!'
exampleZip.close()
