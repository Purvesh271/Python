i = 1
print("Type zero to exit")
while i<=100:
    num = int(input("Enter a number:"))
    if num == 0:
        break
    print(num,"^2=",num**2)
    i+=1
print("End of loop")
