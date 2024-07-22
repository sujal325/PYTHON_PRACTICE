list1 = set([1, 2, 6, 3, 7, 3, 4])
list2 = [2, 4, 2, 3]
count_ = 0
for i in list1:
    if list2.count(i) != 0:
        count_ += 1
    else:
        continue
print(count_)
