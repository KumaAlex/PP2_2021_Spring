x = [int(i) for i in input().split()]
a = set()
b = set()

for i in range(x[0]):
    q = input()
    a.add(q)
for i in range(x[1]):
    q = input()
    b.add(q)

o = list(a.intersection(b))
o.sort()
print(len(o))
for i in o:
    print(i, end = " ")
print(" ")

o1 = list(a.difference(b))
o1.sort()
print(len(o1))
for i in o1:
    print(i, end = " ")
print(" ")

o2 = list(b.difference(a))
o2.sort()
print(len(o2))
for i in o2:
    print(i, end = " ")
print(" ")