# find if the length of a word is even print "even!"
sentence = input("type a sentence here: ").split()
st = sentence
num = 1
for s in st:
    if (num % 2) == 0:
        print(f"{s} even")
    num += 1
