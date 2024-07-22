list_ = [1, 3, 4, 5, 7, 8, 9, 0, 2, 1]
k = list_[0]
for i in list_:
    if i >= k:
        k = i
print(k)
