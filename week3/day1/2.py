x = input().split()
i = 1000
for j in x:
    a = int(j)
    if a < i and a > 0:
        i = a
print(i)