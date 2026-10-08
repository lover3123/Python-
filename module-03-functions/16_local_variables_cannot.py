# Ch3 | 16/41 | Local Variables Cannot Be Used in the Global Scope [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter3

def spam():
    eggs = 31337
spam()
print(eggs)
