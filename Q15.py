n=int(input("Enter number of students: ")) 
d={} 
for i in range(n): 
    roll_no=int(input("Enter roll no: ")) 
    name=input("Enter name: ") 
    marks=int(input("Enter marks: ")) 
    d[roll_no]=[name,marks] 
for k in d: 
    if(d[k][1]>75): 
        print(
            d[k][0])


