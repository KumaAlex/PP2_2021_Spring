x = set(int(i) for i in input().split())
y = set(int(i) for i in input().split())
q = list(x.intersection(y))
q.sort()
for i in q:
    print(i, end = " ")