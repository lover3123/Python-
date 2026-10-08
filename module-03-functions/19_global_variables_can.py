# Ch3 | 19/41 | Global Variables Can Be Read from a Local Scope [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter3

def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
