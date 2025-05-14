def reverse_number(n):
    r=0
    while n>0:
       d=n%10
       r=r*10+d
       n=n/10
    return r
n=int(input("enter the number to be reversed: "))
r=reverse_number(n)
print("reversed number is:",r)