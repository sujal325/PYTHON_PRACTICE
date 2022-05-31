print("Welcome to bill calculater.")
# bill
bill=input("What is your bill: ₹")
# tip
tip=input("How much money you want to give for tip? (10%) (12%) (15%)?:  ")
bill_amount=int(bill)+int(bill)*int(tip)/100
# split_amount
split_amount=input("How many people what's to split bill amount: ")
result=int(bill_amount)/int(split_amount)
# total_amount
print(f"Amount you pay: {result}")