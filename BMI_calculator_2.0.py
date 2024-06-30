print("Welcome to BMI calculator.")
weight = int(input("What is your weight in kilogram(kg): "))
height = float(input("What is your height in meter(m): "))
bmi = weight / height**2
bmi = round(bmi, 2)
print(f"Your BMI is : {bmi}")
if bmi < 18.5:
    print("You are underweight.")
elif bmi > 18.5 and bmi < 25:
    print("Your are normal weight.")
elif bmi > 25 and bmi < 30:
    print("You are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")
