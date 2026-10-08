# Ch10 | 04/24 | Getting the Traceback as a String [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter10

def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')

spam()
