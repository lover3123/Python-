def count_vowels(x):
    vowels=['a','e','i','o','u']
    count=0
    x =x.casefold()
    for i in x:
        if i in vowels:
            count+= 1
    print("the total count of vowels is:", count)
str1 = input("enter the input string:\n")
count_vowels(str1)
