def function(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        print(min(num1, num2))
    elif num1 % 2 == 0 and num2 % 2 != 0 or num1 % 2 != 0 and num2 % 2 != 0:
        print(max(num1, num2))
    else:
        print("I don't know what to do.")


function(int(input("num1: ")), int(input("num2: ")))
