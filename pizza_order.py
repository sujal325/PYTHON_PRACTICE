print("Welcome to pizza store counter.")
size = input(
    "Which pizza do you want medium size (m) , large size (l) or small size (s): "
)
pepperoni = input("Do you want pepperoni yes (y) and no (n): ")
extra_cheese = input("If you want extra cheese (y) for yes and (n) for no: ")
price = 0
if size == "s":
    price = 15
if size == "m":
    price = 20
if size == "l":
    price = 25
if pepperoni == "y":
    if size == "s":
        price += 2
    else:
        price += 3
if extra_cheese == "y":
    price += 1
print(f"Price of your pizza is ${price}")
