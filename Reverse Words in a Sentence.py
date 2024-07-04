def sentence(sen):
    l = sen.split()
    a = " ".join(reversed(l))
    print(a)


sentence(input("sentence: "))
