age = int(input("What is your age?"))
if age>=18:
    print("You are an adult!!")
    gender = input("Are you a Girl or a Boy ? (M/F)")
    if gender=='M' or gender=='m':
        if age>=21:
            print("You are a",age,"year old boy who is eligible for marriage!")
        elif age<=21:    
            print("You are not eligible for marriage...")
        else:    
            print("You are still a minor..")
                    
            
    elif gender=='F' or gender=='f':
        if age>=21:
            print("You are a",age,"year old girl who is eligible for marriage!")
        elif age<=21:    
            print("You are not eligible for marriage...")
        else:    
            print("You are still a minor..")


    


   
