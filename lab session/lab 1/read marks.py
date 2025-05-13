name=input('enter the name of the person:')
usn=input('enter the usn of the student:')
print("")
print('enter marks in 3 subjects')
phy_marks=int(input("enter marks of the first subject:"))
chem_marks=int(input("enter marks of the second subject"))
maths_marks=int(input("enter marks of the third subject:"))

print("")
total=phy_marks + chem_marks + maths_marks
percentage=(total/300)*100
print('name of the student is',name)
print('USN',usn)
print('The total is',total,'and the percentage is',percentage)
print(" ")
if(phy_marks>=40 and chem_marks>=40 and maths_marks>=40):
    print("you are pass")
elif ((phy_marks >= 40 and chem_marks >= 40) or (chem_marks >= 40 and maths_marks >= 40) or (phy_marks >= 40 and maths_marks >= 40)):
    print("student passed in 2 exams")
elif((phy_marks<40 or chem_marks<40 or maths_marks<40)):
    print("student passed in 1 exam")
else:
    print("student failed in all exams")
  