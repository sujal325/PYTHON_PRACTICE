a = dict()
num = 1
while num < 4:
    user = input("Name of friend: ")
    language = input("Favorite language: ")
    a[user] = language
    num += 1
print(f"Printing dictionary: {a}")
