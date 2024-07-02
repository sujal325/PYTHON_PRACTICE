# find word start form letter s or S
sentence = input("Write any sentence and find word start form letter s or S: ")
st = sentence.split()
for l in st:
    if l[0] == "s" or l[0] == "S":
        print(l)
