base =int(input("enter the base value: \n"))
exponent =int(input("enter the exponent value \n"))
result = 1
while exponent != 0:
    #result*= base
    result = result*base
    exponent=exponent-1
print("answer="+str(result))

#calculate power of number usinf a for loop 
base = int(input("Enter the base value : \n"))
exponent = int(input('Enter the exponrnt value : \n'))
result = 1
for exponent in range(exponent, 0, -1):
 result *= base
print("Answer = " + str(result))