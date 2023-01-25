import math
samples=eval(input("Enter a tuple of numeric samples:"))
samples=list(samples)
n=len(samples)
s=0
for xi in samples:
    s+=xi
mean=s/n
t=0
for xi in samples:
    t+=(xi-mean)**2
sd=math.sqrt(t/(n-1))
print("The standard deviation of the given data is : root(",t,"/",n-1,")=",sd)
