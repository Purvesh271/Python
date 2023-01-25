
#(i)
print("(i)")
x = int(input("Enter value of x:"))
n=int(input("Enter value of n:"))
s=0
for i in range(n+1):
    k=x**i
    s=s+k
print(" Sum of the series: 1+x+x^2+x^3+x^4+ ............x^n \n")
print(" with x:",x,"and n:",n,"is=",s)


#(ii)
print("(ii)")
x = int(input("Enter value of x:"))
n=int(input("Enter value of n:"))
s=0
j=0
for i in range(n+1):
    j=(-1)**i
    k=j*(x**i)
    s=s+k
print(" Sum of the series: 1-x+x^2-x^3+x^4+ ............x^n \n")
print(" with x:",x,"and n:",n,"is=",s)


#(iii)
print("(iii)")
x = int(input("Enter value of x:"))
n=int(input("Enter value of n:"))
s=x
j=0
if (n==1):
    print(" Sum of the series: x+x^2/2-x^3/3+x^4/4+ ............x^n/n \n")
    print(" with x:",x,"and n:",n,"is=",s)
else:
    for i in range(2,n+1):
        j=(-1)**i
        k=(j*(x**i))/i
        s=s+k
    print(" Sum of the series: x+x^2/2-x^3/3+x^4/4+ ............x^n/n \n")
    print(" with x:",x,"and n:",n,"is=",s)

#(iv)
print("(iv)")    
x = int(input("Enter the value of x:"))
n=int(input("Enter value of n:"))
s=x
j=1
fact=1
if (n==1):
    print(" Sum of the series: x+x^2/2!-x^3/3!+x^4/4!+ ............x^n/n! \n")
    print(" with x:",x,"and n:",n,"is=",s)
else:
    for i in range(2,n+1):
        fact=fact*i
        j=(-1)**i
        k=((j*(x**i))/fact)
        s=s+k
    print(" Sum of the series: x+x^2/2!-x^3/3!+x^4/4!+ ............x^n/n! \n")
    print(" with x:",x,"and n:",n,"is=",s)
    




