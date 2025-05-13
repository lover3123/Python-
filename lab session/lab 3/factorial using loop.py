#using while loop 
n=int(input("enter the number to find factorial: "))
fact=1
i=1
if n < 0:
    print("Enter a positive integer!")
elif n == 0 or n == 1:
    print("The factorial of the number is: 1")
else:
    while i <= n:
        fact = fact * i
        i = i + 1
    print("The factorial of the number is", fact)
