def is_digit(x):

    digit = 0
    char = 0
    for i in x:
        if i.isdigit():
            digit += 1
        else:
            char += 1
    print("the total number of digits is:", digit)
    print("the total number of non-digit characters is:", char)  # Write your code here :-)

x = input("enter the string \n")
is_digit(x)