# find number divisible by 3
number = int(input("chose number: "))
for num in range(1, number):
    if (num % 3) == 0:
        print(num)
