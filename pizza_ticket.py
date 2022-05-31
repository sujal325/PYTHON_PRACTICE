print("Welcome to pizza counter.")
size=input("Which size of pizza do you want? s,m or l ? ")
bill=0
if size=="s":
    bill+=100
elif size=="m":
    bill+=200
elif size=="l":
    bill+=300
peproni=input("Do you want paproni? y or n ? ")
if peproni=="y":
    if size=="s":
        bill+=30
    else:
        bill+=50
chease=input("Do you want some extra chease? y or n ? ")
if chease=="y":
    if size=="s":
        bill+=50
    else:
        bill+=90
print(f"Your bill is ₹{bill}")
