print("Welcome to love calculater.")

her=input("What is her name? ")
his=input("What is his name? ")
add=her+his

lower_case=add.lower()

t=add.count("t")
r=add.count("r")
u=add.count("u")
e=add.count("e")
true=t+r+u+e

l=add.count("l")
o=add.count("o")
v=add.count("v")
e=add.count("e")
love=l+o+v+e

true_love=str(true)+str(love)

print(f"This is your love score {true_love}")


