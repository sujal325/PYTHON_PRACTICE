print(
    "Welcome to this program in which you give a number and this program add all the even number till your given number."
)
num = int(input("Write a number: "))
total = 0
for num1 in range(0, num + 1):
    if num1 % 2 == 0:
        total += num1
print(f"Result you get by adding all even number is: {total}")
