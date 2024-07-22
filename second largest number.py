n = [1, 2, 3, 4, 7, 3, 6, 9, 8, 6]
z = n[0]
for i in n:
    if i >= z:
        z = i
s = n[0]
for i in n:
    if s <= i < z:
        s = i
print(s)