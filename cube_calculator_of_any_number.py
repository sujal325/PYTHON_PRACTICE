print("WELCOME TO SQUARE // CUBE CALCULATER.")
print(
    """
    IF YOU WANT SQUARE TYPE 1
    ELSE TYPE 2
"""
)


key = input("DO YOU WANT TO CALCULATE SQUARE OF CUBE: ")
num = int(input("WHICH NUMBER SQUARE // CUBE DO YOU WANT: "))


def square(x):
    result = x**2
    print(f"square of {x} is {result}")


def cube(x):
    result = x**3
    print(f"cube of {x} is {result}")


if key == "1":
    square(num)
else:
    cube(num)
