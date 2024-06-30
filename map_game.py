print("Welcome to map game")
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Write your position here like (a2 - b1 - c3) :: ")
letter = position[0]
abc = ["a", "b", "c"]
letter_value = abc.index(letter)
number_value = int(position[1])
map[number_value][letter_value] = "x"
print(f"{line1}\n{line2}\n{line3}")
