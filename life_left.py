print(
    "Welcome to this calculator which calculate how much time you left.This looks funny but I substrace you age with average age a human live and cunvert it to weeks."
)
age = int(input("What is your current age: "))
years_left = int(73.4 - age)
weeks_left = int(years_left * 52)
days_left = int(years_left * 365)
print(
    f"\nYou have almost\ndays left: {days_left} \nweeks left: {weeks_left}\nyears left: {years_left}"
)
