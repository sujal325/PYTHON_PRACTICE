import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image=[rock,paper,scissors]
print("Welcome to ROCK PAPER SCISSORS GAME.")
user=int(input("What did you choose? 0 for ROCK,1 for PAPER,2 for SCISSORS: "))
print("you choose")
print(game_image[user])
result=0
computer=random.randint(0,2)
print("computer choose")
print( game_image[computer])
if (user==computer):
   result="YOU DROW"
elif (user==0 and computer==2)or(user==2 and computer==1)or(user==1 and computer==0):
   result="YOU WIN"
else:
    result="YOU LOSE"
print(F"{result} this game.")