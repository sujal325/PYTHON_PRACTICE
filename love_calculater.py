print("Welcome to love calculater")
name1 = input("Write your name: ")
name2 = input("write your patner name: ")
combinename = name1 + name2
lower_case_combinename = combinename.lower()

t = lower_case_combinename.count("t")
r = lower_case_combinename.count("r")
u = lower_case_combinename.count("u")
e = lower_case_combinename.count("e")

true = t + r + u + e


l = lower_case_combinename.count("l")
o = lower_case_combinename.count("o")
v = lower_case_combinename.count("v")
e = lower_case_combinename.count("e")

love = l + o + v + e

score = int(str(true) + str(love))
if 10 > score > 90:
    print(f"Your score is {score},you both are like coke and mentos.")
elif 60 > score > 40:
    print(f"Your score is {score},you are alright together.")
else:
    (f"your score is {score}")
