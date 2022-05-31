print("Welcome to BMI claculater.")
height=float(input("What is your height: "))
weight=float(input("What is your weight: "))

result=weight/height**2
if result<18.5:
    print(f"Your BMI is this {result}.You have underweight.")
if 18.5<result<25:
    print(f"Your BMI is this {result}.You have a normal weight.")
elif 25<result<30:
    print(f"Your BMI is this {result}.You are overweight.")
elif 30<result<35:
    print(f"Your BMI is this {result}.You are in category of obese.")
else:
    print(f"Your BMI is this {result}.You are clinicaly obese.")

