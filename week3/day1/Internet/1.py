x = int(input())
y = int(input())
z = str(input())
if len(z) != 1:
    print("Unknown operation")
else:
    if z == "*":
        print(x*y)
    elif z == "-":
        print(x-y)
    elif z == "+":
        print(x+y)
    elif z == "/":
        print(x/y)
    else:
        print("Unknown operation")