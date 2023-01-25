l =input("Enter a line:")

lowercount = uppercount =0
vowelcount = consonantcount =0

for a in l:
    if a.islower():
        lowercount+=1
    elif a.isupper():
        uppercount+=1
    if (a in ('a','e','i','o','u','A','E','I','O','U')):
        vowelcount+=1
    elif(a in('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t',
              'v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N',
              'P','Q','R','S','T','V','W','X','Y','Z')):
        consonantcount+=1


print("Number of uppercase letters:",uppercount)
print("Number of lowercase letters:",lowercount)
print("Number of vowels:",vowelcount)
print("Number of consonants:",consonantcount)
    
        

