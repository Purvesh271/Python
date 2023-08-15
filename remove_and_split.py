def remove_and_split(string,word):
    newstr = string.replace(word,"")
    return newstr.strip()
t = "   hello world   "
n =remove_and_split(t,"world")
print(n)