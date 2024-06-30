print("Welcome to rollercoaster ticket center.")
height = int(input("What is your height: "))
age = int(input("What is your age: "))
if height >= 120:
    if age > 18:
        print("You can ride and your ticket price is $12.")
    else:
        print("You can ride and your ticket price is $7.")
else:
    print("You can't ride you are short to ride rollercoaster.")
