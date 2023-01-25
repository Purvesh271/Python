num = int(input("Enter a number:"))
lim =int(num/2)+1
for i in range(2,lim):
    r = num%i
    if r==0:
        print(num,"is a composite number")
        break

else:
    print(num,"is a prime number")
        

