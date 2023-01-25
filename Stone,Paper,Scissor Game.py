import random
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp == 'stone':
        if you == 'sissor ':
            return False
        elif you == 'paper':
            return True
    elif comp == 'sissor':
        if you== 'paper':
            return False
        elif you == 'stone':
            return True
    elif comp == 'paper':
        if you== 'stone':
            return False
        elif you == 'sissor':
            return False

print("Comp Turn : stone paper scissor?")
randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    comp ='stone'
elif randNo == 2:
    comp = 'paper'
elif randNo == 3:
    comp = 'scissor'

you = input("Your Turn : stone paper scissor?\n")

a = gameWin(comp,you)

print(f"Computer chose:{comp}")
print(f"You chose:{you}")
if a==None:
    print("TIE!")
elif a:
    print("YOU WIN XD")
else:
    print("YOU LOSE XO")