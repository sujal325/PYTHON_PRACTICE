user = int(input("Which number factorial do you want: "))
num = user
result = 1
while num >= 1:
    result *= num
    num -= 1
print(f"You got {result}")
