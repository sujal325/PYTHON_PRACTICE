print("Welcome to rollercoaster ticket center.")
height = int(input("What is your height: "))
age = int(input("What is your age: "))
photo = input(
    "Do you want a photo while riding rollercoaster (y) for yes and (n) for no: "
)
ticket = 0
if height >= 120:
    if age > 18:
        ticket = 12
        if age > 45 and age < 55:
            ticket = 0
            print("\nFor you this ride is free.")
    else:
        ticket = 7
    if photo == "y":
        ticket += 3
        print(f"Your ticket price is ${ticket}")
    else:
        print(f"\nYou can ride and your ticket price is ${ticket}.")
else:
    print("You can't ride you are short to ride rollercoaster.")

