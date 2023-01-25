a = input("Enter the first number:")
b = input("Enter the second number:")
c = input("Enter the third number:")


if a>b>c:
    print(a,"is the larget number and ",c,"is the smallest number")

elif a>c>b:
    print(a,"is the largest number and ",b,"is the smallest number")

elif b>a>c:

    print(b,"is the largest number and ",c,"is the smallest number")

elif b>c>a:
    print(b,"is the largest number and ",a,"is the smallest number")

elif c>b>a:
    print(c,"is the largest number and ",a,"is the smallest number")

elif c>a>b:
    print(c,"is the largest number and ",b,"is the smallest number")

else:
    print("all are equal")
    
