print("Welcome to leap year finder.")
year = int(input("Which you want to find is a leap year or not: "))
find = year % 4
if find == 0:
    find = year % 100
    if find == 0:
        find = year % 400
        if find == 0:
            print("This is a leap year.")
        else:
            print("This is not a leap year.")
    elif find != 0:
        print("This is a leap year.")
else:
    print("This not a leap year.")
