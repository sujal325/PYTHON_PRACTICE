print("Just playing with class.")


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


name = input("What is your name: ")
age = input("What is your age: ")
letter = person(name, age)
print(f"Your name is {letter.name} and your age is {age}.")
