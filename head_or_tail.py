import random

print("Welcome to toss generater")
random_integer = random.randint(0, 1)
if random_integer == 1:
    print("\nYou got head")
else:
    print("\nYou got tail")
