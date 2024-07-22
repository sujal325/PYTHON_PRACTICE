a = 48
b = 18
r = 0
while a % b != 0:
    r = a % b
    a = b
    b = r

print(r)
