def num(num1, num2):
    if num1 == 20 or num2 == 20:
        print(True)
    elif num1 + num2 == 20:
        print(True)
    else:
        print(False)


num(int(input("num1: ")), int(input("num2: ")))
