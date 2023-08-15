a =int(input("enter the first number:"))
b =int(input("enter the second number:"))
c =int(input("enter the third number:"))

if a>b and a>c:
    print("first number is greater than both second number and third number")
elif b>a and b>c:
    print("second number is greater than both first number and third number")
elif c>a and c>b:
    print("third number is greater than both first number and second number")
else :
    print("Either any two or all the three numbers are equal")