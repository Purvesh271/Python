num = int(input("Enter the number:"))
prime=True

for i in range(2,num):
    if(num%i ==0):
       prime = False
       break
if prime:
     print("It is a prime number")
else:
    print("It is not a prime number")