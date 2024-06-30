print("welcome to tabel builder from 1 to infinity.")


def tabel(x):
    digit = 1
    result = 0
    while digit <= 10:
        result = x * digit
        print(f"{x} X {digit} = {result}")
        digit += 1


num = int(input("Which number tabel do you want: "))
tabel(num)