print("Welcome to xyz insurance compary.")
print("Fullfill your detail for insurance.")
name=input("What is your name: ")
gender=input("what is your gender: ")
married=input("Are you married: ")
age=int(input("What is your age: "))
result=0
if (gender=="male of Male"and age>30)or (gender=="female or Female"  and age>25)or( married=="yes or no or Yes or No"):
    result="Insured"
else:
    result="Not Insured"
print(f"{name} you are {result}.")