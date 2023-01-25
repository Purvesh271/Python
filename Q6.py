n = int(input("Enter any number: "))

#For Perfect Number

sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("1: The number ",n,"is a Perfect number!")
else:
    print("1: The number ",n,"is not a Perfect number!")

#For Armstrong Number
#calculated the length (number of digits)
order = len(str(n))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = n
while (temp <0):
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if n == sum:
   print("2: The number ",n,"is an Armstrong number")
else:
   print("2: The number ",n,"is not an Armstrong number")

#For Palindrome Number
k=n
temp=n
rev=0
while(k>0):
    dig=k%10
    rev=rev*10+dig
    k=k//10
if(temp==rev):
    print("3: The number",n," is a palindrome!")
else:
    print("3: The number",n," isn't a palindrome!")
