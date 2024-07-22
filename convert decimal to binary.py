number_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_list=[]
for i in number_list:
    bn=bin(i)[2:]
    binary_list.append(bn)
print(binary_list)