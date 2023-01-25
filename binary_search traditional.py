'''
Name of the program:
size of the program:
IDE used:
python interpreter version used:\
'''

#arr = eval(input('enter a list of numbers'))
arr = [54,2,3,12,4,13,65,28,26,84]
arr.sort()
print(arr)

ele= int(input("enter the search element:"))
beg,last = 0,len(arr)-1

while beg<=last:
    mid = (beg+last)//2
    if arr[mid]==ele:
        print("element is found at postion=",mid+1)
        break
    elif ele>arr[mid]:
        beg = mid+1
    elif ele<arr[mid]:
        last = mid-1
if beg>last:
    print("element not found!")
