y=input("enter the name of the person: \n")
x=int(input("enter the year of birth: \n"))
current_year =int(input("enter current year: \n"))
age = current_year - x
if(age>=60):
    print("you are senior citizen")
else:
    print("you are not senior citizen")
