def sum():
    user = int(input("Write integer till you want to get sum: "))
    num = 0
    for i in range(1, user + 1):
        num += i
    print(f"sum of integer: {num}")


sum()
