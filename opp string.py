rows=4
for i in range(1,rows):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
    

st = input ("Enter a string :")
size = len (st)
for i in range(size,0,-1):
    print(st[i-1])

for i in range (len(st),0,-1):
    print(st[i-1],end="")

for i in range (len(st)):
    print(st[i],":",i,":",i-len(st))
    
