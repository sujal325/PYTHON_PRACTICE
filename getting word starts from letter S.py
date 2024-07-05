user = input("Write names: ").split()
for i in user:
    if i[0] == "s" or i[0] == "S":
        print(i)
    else:
        continue
