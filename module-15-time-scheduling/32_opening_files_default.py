# Ch15 | 32/37 | Opening Files with Default Applications [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
# OUT: 12
fileObj.close()
import subprocess
subprocess.Popen(['start', 'hello.txt'], shell=True)
