import random
number = random.randint(10,20)
ctr =0
while ctr<5:
    guess =int(input("Guess a number in range 10-30:"))
    if guess==number:
        print("YOU WIN :)")

        break
    else:
        ctr+=1
if not ctr <5:
    print("YOU LOSE :( \n The number was",number)
    
