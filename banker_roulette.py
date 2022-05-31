import random
print("Welcome to game of bank roulette.The which have card pay the bill.")
name_of_player=input("What is name of player? Write your names: ")
split_name=name_of_player.split(" ")
x=len(split_name)
random_name=random.randint(0, x-1)
final_name=split_name[random_name]
print(final_name+" "+"you will pay this bill.")