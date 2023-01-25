#Python program to compute simple interest and compound interest.

p = float(input("Enter the Principal Amount :"))
r = float(input("Enter the Rate Of Intrest  :"))
t = float(input("Enter Time period in Years :"))

si = (p*r*t) / 100
ci = pow((1 + r / 100),t) *p - p 

print("Simple Intrest is =" ,si)
print("Compound Intrest is =" ,ci)
