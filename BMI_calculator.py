print("Welcome to BMI calculator.")
weight = int(input("What is your weight in kilogram(kg): "))
height = float(input("What is your height in meter(m): "))
bmi = weight / height**2
bmi = round(bmi, 2)
print(f"Your BMI is :{bmi}")
