a = int(input("Enter length of side1:"))
b = int(input("Enter length of side2:"))
c = int(input("Enter length of side3:"))

if((a+b) > c and (b+c) > a and (a+c) > b):
    print("Valid Triangle")
    if(a == b == c):
        print("Equilateral Triangle")
    elif(a == b or a == c or b == c):
        print("Isoceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a Triangle")