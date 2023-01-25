# part (i)
numList = eval(input("Enter a list of numbers (Enclosed within square brackets) : "))
big = numList[1]
length = len(numList)
i = 0
while i < length:
    res = numList[i]
    i += 1
if res > big:
    print("The biggest number is : ", res)
else:
    print("The biggest number is : ", big)

# part (ii)
List = eval(input("Enter a list : "))
print("Original List is:", List)
length1 = len(List)
if length1 % 2 != 0:  #checking condition
    length1 -= 1
for i in range(0, length1, 2):
    List[i], List[i+1] = List[i+1], List[i]  #swapping values
print("List after swapping :", List)
