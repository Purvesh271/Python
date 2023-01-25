n =input("Enter a string:")
N=n.lower()
y=0

for j in range(0,len(N)):
   if N[j]!=N[len(N)-j-1]:
      y=1
if y==0:
   print("Given number is a palindrome")
else:
   print("Given number is not a palindrome")

print("String with converted case is :",n.swapcase())
