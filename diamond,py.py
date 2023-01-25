rows = 5
p = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, p):
        print(end=" ")
    p = p - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
p = rows - 2

for i in range(rows, -1, -1):
    for j in range(p, 0, -1):
        print(end=" ")
    p = p + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
