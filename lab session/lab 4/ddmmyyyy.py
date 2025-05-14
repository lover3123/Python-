def date1(date):
    dd, mm, yyyy = date.split("/")
    dd = int(dd)
    mm = int(mm)
    yyyy = int(yyyy)
    if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
        max1 = 31
    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
        max1 = 30
    elif yyyy % 4 == 0 and (yyyy % 100 != 0 or yyyy % 400 == 0):
        max1 = 29
    else:
        max1 = 28

    if mm < 1 or mm > 12:
        return 'month is invalid'
    elif dd < 1 or dd > max1:
        return 'date is invalid'
    elif dd == max1 and mm < 12:
        dd = 1
        mm = mm + 1
        return f"incremented date is: {dd:02d}/{mm:02d}/{yyyy}"
    elif dd == 31 and mm == 12:
        dd = 1
        mm = 1
        yyyy = yyyy + 1
        return f"incremented date is: {dd:02d}/{mm:02d}/{yyyy}"
    else:
        dd = dd + 1
        return f"incremented date is: {dd:02d}/{mm:02d}/{yyyy}"

date = input('enter the date (dd/mm/yyyy): ')
result = date1(date)
print(result)
