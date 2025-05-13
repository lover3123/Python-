'''def spam():
    print(eggs) #ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()'''

'''If you run the previous program, it produces an error message. 
Traceback (most recent call last):
  File "C:/test3784.py", line 6, in <module>
    spam()
  File "C:/test3784.py", line 2, in spam
    print(eggs) # ERROR!
 UnboundLocalError: local variable 'eggs' referenced before assignment'''

