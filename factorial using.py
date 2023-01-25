'''Q.4. Write a program to find the factorial of a number using while loop.'''
num = int(input("Enter the number: "))
fact=1
i = 1
while i<=num:
    fact = fact*i
    i = i +1
print("The factorial of ",num,"=",fact)