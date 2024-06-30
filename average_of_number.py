print("Welcome to average calculating calculater")
numbers = input(
    "numbers you want to average out (numbers should be saprated by space): "
).split()
total = 0
times = 0
for i in numbers:
    num = int(i)
    print(total)
    times += 1
average = total / times
print(f"The average of all numbers is: {average}")
