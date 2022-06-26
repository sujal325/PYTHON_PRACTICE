add=0
for n in range(0,101):
  if (n%5)and(n%3)==0:
    print('fizzbuzz')
  elif (n%3)==0:
    print('fizz')
  elif (n%5)==0:
    print('buzz')
  else:
    print(n)