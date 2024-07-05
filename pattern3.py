# ******
# *    *
# *    *
# *    *
# ******
user = int(input("Number of lines do you want: "))
for i in range(1, user + 1):
    if i == 1:
        print("*" * user)
    elif i == user:
        print("*" * user)
    else:
        print("*" + " " * (user - 2) + "*")
