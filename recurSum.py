def recurSum(n): 
    if n <= 1: 
        return n 
    return n + recurSum(n - 1)
n = int(input("Enter the value of n:"))
print(recurSum(n))