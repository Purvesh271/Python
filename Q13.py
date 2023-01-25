a = eval(input("Enter a list/tuple of some elements : "))  #taking input
a = list(a)
length = len(a)
ask = eval(input("Enter the element you want to search for : "))
for i in a:  # Searching element
    if i == ask:
        res = a.index(i)   # figuring out position of the particular element
        print("Element found at position : ", res + 1)  #printing result
        break
