binary_numbers = [
    "1",  # Binary representation of 1
    "10",  # Binary representation of 2
    "11",  # Binary representation of 3
    "100",  # Binary representation of 4
    "101",  # Binary representation of 5
    "110",  # Binary representation of 6
    "111",  # Binary representation of 7
    "1000",  # Binary representation of 8
    "1001",  # Binary representation of 9
    "1010",  # Binary representation of 10
]
list_ = []
for i in binary_numbers:
    number = int(i, 2)
    list_.append(number)
print(list_)