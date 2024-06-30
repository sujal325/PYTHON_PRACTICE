import random

print("Welcome to random name selector program")
names = ["sujal", "shresth", "poddar"]
number_of_names = len(names)
random_name = random.randint(0, number_of_names - 1)
print(f"\nRandom name generated is {names[random_name]}")
