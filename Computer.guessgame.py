import random
print('guess a number between 0 and 10000')

a=0
b=10000

while True :
    d=range(a,b)
    e=random.choice(d)
    print(f'is your guess higher or lower or equal to {e}?')
    f = input('H , L , E?')
    f= f.upper()
    
    if f == 'H':
        a=e
    elif f == 'L':
        b=e
    else:
        print('yay!!!! i guessed your number')
        break
