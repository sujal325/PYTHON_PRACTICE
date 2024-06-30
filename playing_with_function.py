print("Just playing with python function.")


def sujal(name, age):
    print(f"your name is {name} and your age is {age}.")


def friends(*friend_s):
    print(f"Name of your friends: {friend_s}")


name_ = input("What is your name: ")
age_ = input("What is your age: ")
name_s = input("Names of your friends: ").split()
sujal(name_, age_)
friends(name_s)
