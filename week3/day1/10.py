n = int(input())
d = {}
for i in range(n):
    a, b = input().split()
    d[a] = b
x = input()
try:
    print(d[x])
except:
    for a, b in d.items():
        if b == x:
            print(a)
            exit()