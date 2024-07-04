string = input("WRITE A SENTENCE: ")

if "  " in string:
    string = string.replace("  ", " ")
    print(string)
else:
    print("double space not detect.")
