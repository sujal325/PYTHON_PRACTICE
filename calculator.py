print(
    "Welcome to this calculator where you can add (+) , substract (-) , multiply (*) and divide (/) any number.\n"
)
instruction = input(
    "You want to add (+) , substract (-), multiplication (*)  OR divide (/): "
).lower()


try:
    num1 = int(input("What is your first number: "))
    num2 = int(input("What is your second number: "))
except:
    print("Only numbers can be calculated.")

result = 0

try:
    if instruction == "+" or instruction == "add":
        result = num1 + num2
    elif instruction == "substract" or instruction == "-":
        result = num1 - num2
    elif instruction == "multiply" or instruction == "*":
        result = num1 * num2
    elif instruction == "divide" or instruction == "/":
        result = num1 / num2
        result = round(result, 2)
    else:
        print("Sorry we can't do this operation is this program.")
except:
    print("")
print(f"Your result is {result}")
