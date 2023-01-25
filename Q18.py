L=[]
M=[]
N=[]
print("Enter any three numbers for the first list in three different lines:")
for i in range(1,4):
    L.append(int(input()))
print("Enter any three numbers for the second list in three different lines:")    
for j in range(1,4):
    M.append(int(input()))
for k in range(0,3):
    N.append(L[k]+M[k])
print("Given lists:",L,M,"Expected output:",N,sep="\n")
