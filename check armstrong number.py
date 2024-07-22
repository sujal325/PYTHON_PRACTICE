number = 157
str_number = str(number)
length = len(str_number)
list_number = set(str_number)
arm = 0
armstrong = 0
for i in list_number:
    r = int(i)
    arm = r**length
    armstrong += arm
print(armstrong)
