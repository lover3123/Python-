# using for loop
n = int(input("enter any number: "))
if n < 0:
    print("enter the positive number")
elif n == 0 or n == 1:
    print("the factorial of a number is: 1")
else:
    fact = 1
    for i in range(n, 0,-1):
        fact = fact * i
    print("the factorial of a number is", fact)