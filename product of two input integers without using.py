'''Q.3. Write a program to calculate the product of two input integers without using * operator. '''
n1 = int(input("Enter the first nummber"))
n2 = int(input("Enter the second number:"))
product = 0
i =n1
while i >0:
    i = i-1
    product = product+n2
print("product of ",n1,"and",n2,"is",product)
