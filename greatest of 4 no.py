a = int(input("Enter number1:"))
b = int(input("Enter number2:"))
c = int(input("Enter number3:"))
d = int(input("Enter number4:"))

if a>b and  a>c and a>d:
    print("number1 is the greatest number")
elif b>a and b>c and b>d :
    print("number2 is the greatest number")
elif c>a and c>b and c>d:
    print("number3 is the greatest number")
elif d>a and d>b and d>c:
    print("number4 is the greatest number")
else:
    print("All are equal")
