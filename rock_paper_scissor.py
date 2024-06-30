import random

print("Welcome to rock paper scissors game")
rps = int(input("Choose 0 for rock , 1 for paper , 2 for scissor: "))
rps_random = random.randint(0, 2)


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print(rps)
if rps == 0:
    print(rock)
elif rps == 1:
    print(paper)
else:
    print(scissors)

print(rps_random)
if rps_random == 0:
    print(rock)
elif rps_random == 1:
    print(paper)
else:
    print(scissors)


if (
    (rps == 0 and rps_random == 0)
    or (rps == 1 and rps_random == 1)
    or (rps == 2 and rps_random == 2)
):
    print("MATCH DRAW")
elif (
    (rps == 0 and rps_random == 1)
    or (rps == 1 and rps_random == 2)
    or (rps == 2 and rps_random == 0)
):
    print("YOU LOOSE")
else:
    print("You win")
