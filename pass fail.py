s1 = int(input("Enter the marks obtained in English:"))
s2 =int(input("Enter the marks obtained in Maths:"))
s3 =int(input("Enter the marks obtained in Science:"))
total =(s1+s2+s3)/3

if s1<35 and s2<35 and s3<35:
    print("You are failed :(")
elif total<40:
    print("You are failed :(")
else :
    print("You are passed :)")