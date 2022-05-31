print("To see your result write your percentage.")
percentage=float(input("What is your percentage? "))
result=0
if percentage>=60:
    result="First divison"
if 59>=percentage>=50:
    result="Second divison"
if percentage<=40:
    result="Fail"
print(f"This is your result {result}")
