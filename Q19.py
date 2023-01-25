D=dict()
n=int(input("Enter the number of teams:"))
for i in range(0,n):
    print("Enter the name of team:",i+1)
    k=input()
    w=int(input("No. of wins:"))
    l=int(input("No. of loss:"))
    D[k]=[w,l]
print("Team name:[WIN,LOSS]=>",D)
#(a)
t=input("Which teams winning percentage? :")
print("WINNING percentage=",(D[t][0])/((D[t][0])+(D[t][1]))*100,"%")
#(b)
print("List of number of wins of each team:",end="")
p=D.values()
L=[]
for j in p:
    L.append(j[0])
print(L)
#(c)
print("List of teams having winning  record,i.e. games won>0:",end="")
M=[]
for k in D:
    M.append(k)
    if D[k][0]==0:
        M.remove(k)
print(M)
