'''def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))'''

''' 21.0
 3.5
 Traceback (most recent call last):
  File "C:/zeroDivide.py", line 6, in <module>
    print(spam(0))
  File "C:/zeroDivide.py", line 2, in spam
    return 42 / divideBy
 ZeroDivisionError: division by zero'''

#ZeroDivision Error
'''def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
 print(spam(2))
 print(spam(12))
 print(spam(0))
 print(spam(1))'''

#o/p 
''' 21.0
 3.5
 Error: Invalid argument.
 None
 42.0'''

'''  Note that any errors that occur in function calls in a try block will also 
be caught. Consider the following program, which instead has the spam() 
calls in the try block:
 def spam(divideBy):
    return 42 / divideBy
 try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
 except ZeroDivisionError:
    print('Error: Invalid argument.')
 When this program is run, the output looks like this:
 21.0
 3.5
 Error: Invalid argument'''