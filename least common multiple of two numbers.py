a = 48
b = 18
mul = abs(a * b)
while a % b != 0:
    r = a % b
    a = b
    b = r
lcm = mul / r
print(lcm)
