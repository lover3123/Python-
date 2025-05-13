def spam():
    global eggs
    eggs = 'spam'  # this is a global variable

def bacon():
    eggs = 'Bacon'  # this is a local
    print(eggs)  # using the local variable

def ham():
    print(eggs)  # this is the global

eggs = 42  # Initialize eggs globally to avoid potential NameError
spam()
print(eggs)
