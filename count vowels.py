def vowels():
    string_1 = "his name is sujal"
    num = 0
    for i in string_1:
        if i == "a" or i == "o" or i == "u" or i == "i" or i == "e":
            num += 1
    print(f"number of vowels in given string is: {num}")


vowels()
