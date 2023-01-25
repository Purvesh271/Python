L=[]
y=1
while y==1:
    s=0
    n=int(input("Enter a number to check if it is a armstrong number:"))
    p=n
    while p>0:
        s+=(p%10)**3
        p=p//10
    if s==n:
        L.append(n)
        L.sort()
    y=int(input("for continue inputting,enter1,else0 :"))
print("out of the given numbers, list of armstrong number:",L,sep="\n")
try:
    print("smallest armstrong number:",L[0],"largest armstrong number:",L[len(L)-1],sep="\n")
except:
    print("no number wa armstrong among the given ones")
