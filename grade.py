marks = int(input("Enter your marks:"))

if marks>= 90:
    grade = "A+"
elif marks>= 80:
    garde= "A"
elif marks>= 70:
    garde= "B"
elif marks>= 60:
    garde= "C"
elif marks>= 50:
    garde= "D"
else:
    grade = "F"

print("Your grade is: ",grade)