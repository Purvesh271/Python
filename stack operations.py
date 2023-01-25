def push():
    item = input("enter an element:")
    stack.append(item)

def pop():
    if stack ==[]:
        print("print stackunderflow!")
        item=None
    else:
        item = stack.pop()
    return item

#_main_
stack = []
while True:
    print("stack operations")
    print("1.push")
    print("2.pop")
    print("3.traverse")
    print("4.exit")
    ch = int(input("enter ur choice:"))
    if ch==1:
          push()
          print(stack)
    elif ch==2:
          item= pop()
          print("item popped",item)
          print(stack)
    elif ch==3:
          print(stack)
    else:
          print("Thanks XD")
          break
    
