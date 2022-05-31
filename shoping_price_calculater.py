print("Welcome to my shop.")
product=input("How many product you buy: ")
price=int(input("What is price of you product: ₹"))
discount=0
if price>=1000:
    discount=price-price*10/100
elif price>=4500:
    discount=price-price*20/100
elif price>=6000:
    discount=price-price*25/100
elif price>=9500:
    discount=price-price*30/100
else:
    discount=price
print(f"You pay ₹{discount}")
    
