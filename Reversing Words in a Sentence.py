def number(num):
    return (abs(100 - num) <= 10) or (abs(200 - num) <= 10)


print(number(int(input("number: "))))
