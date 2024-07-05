user = int(input("Give integer: "))
i = 2
while i < user:
    num = user % i
    if num == 0:
        print("It is not prime number.")
        break
    i += 1
if num != 0:
    print("It is a prime number")
