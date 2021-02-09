x = input()
i = len(x)
while i != 0:
    i -= 1
    y = x.replace("  "," ")
    if y == x:
        break
    x = y
print(x)