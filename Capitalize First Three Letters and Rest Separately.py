def word(w):
    answer = w[:3].capitalize() + w[3:].capitalize()
    print(answer)


word(input("word: "))
