print("This is made to determine number is even or odd.")
num = int(input("Give a number which you want to determine it is even or odd: "))
output = num % 2
if output == 0:
    print("It is a even number.")
else:
    print("It is a odd number.")
