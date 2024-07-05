def greatest():
    a = int(input("Write first integer: "))
    b = int(input("Write second integer: "))
    c = int(input("Write third integer: "))
    if (a > b) and (a > c):
        print(f"{a} is greatest.")
    if (b > a) and (b > c):
        print(f"{b} is greatest.")
    if (c > a) and (c > b):
        print(f"{c} is greatest.")


greatest()
