# Ch9 | 07/23 | Permanently Deleting Files and Folders [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter9

import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        os.unlink(filename)
