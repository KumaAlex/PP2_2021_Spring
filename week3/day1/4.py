x = input().split()
q = 0
for i in x:
    if i != "0":
        print(i, end = " ")
        q += 1
for i in range(q, len(x)):
    print("0", end = " ")