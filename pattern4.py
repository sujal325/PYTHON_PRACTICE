#     *
#    ***
#   *****
#  *******
# *********
user = int(input("Number of lines do you want: "))
for i in range(1, user + 1):
    print(" " * (user - i), end="")
    print("*" * (2 * i - 1), end="")
    print("")
