n=input("Enter the phone number:")
if len(n)==12:
    s=n.split("-")
    if len(s[0])==3 and len(s[1])==3 and len(s[2])==4:
        if s[0].isdigit() and s[1].isdigit() and s[2].isdigit():
            print("phone number is valid")
else:
    print("phone number is invalid")
