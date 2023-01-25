weight=eval(input("Enter the weight of he person in kg:"))
height=eval(input("Enter the height of he person in m:"))
bmi=weight/(height)**2
if bmi<=18.5:
    print("You are underweight!!")
elif bmi<=24.9:
    print("You are taking a good diet...XD")
elif bmi<=29.9:
    print("You are overweight :(")
else:
    print("You are obesed and need to control your diet")
