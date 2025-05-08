while True:
    print('who are you?')
    name=input()
    if name != 'joe':
        continue
    print('hello, joe. what is the password?(it is a fish)')
    password = input()
    if password == 'fish':
        break
print('access granted')