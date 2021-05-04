import random
def gamewin(comp,b):
    if comp==b:
        return None

# checking the condition againest computer
    elif comp=='s':
        if b=='w':
            return False
        elif b=='g':
            return True

    elif comp=='g':
        if b=='s':
            return False
        elif b=='w':
            return True

    elif comp=='w':
        if b=='g':
            return False
        elif b=='s':
            return True

print('comp turn: snake(s),water(w) or gun(g)')
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'

b=input('player2 turn: snake(s),water(w) or gun(g)')

a = gamewin(comp,b)
print(f'computer choose {comp}')
print(f'you choose {b} ')


if a==None:
    print('the game is a tie!')
elif a:
    print('you win!')
else:
    print('you lose!')