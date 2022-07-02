print('welcome to name score game.')
name=input('Type your name: ')
score=0
for l in name:
    if l=='a' or l=='r' or l=='p' or l=='s':
        score+=10
    elif l=='d' or l=='k':
        score+=9
    elif l=='l' or l=='j' or l=='m':
        score+=8
    elif l=='n' or l=='u' or l=='v':
        score+=7
    elif l=='z':
        score+=6
    elif l=='f' or l=='b':
        score+=5
    elif l=='w' or l=='t':
        score+=4
    elif l=='w' or l=='x' or l=='e' or l=='c':
        score+=3
    elif l=='q' or l=='o' or l=='h' or l=='i':
        score+=2
    elif l=='g' or l=='y' or l=='' or l=='':
        score+=1
    else:
        score+=0
result=0
if score>=35:
    result='you win this game'
else:
    result='With this name you loose this game'
print(f'\n{result}. (you score is {score})')