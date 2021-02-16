x = [int(i) for i in input().split()]
a = set()
b = set()

for i in range(x[0]):
    a.add(int(input()))
for i in range(x[1]):
    b.add(int(input()))

def func(o):
    print(len(o))
    o.sort()
    for i in o:
        print(i, end = " ")
    print()        

func(list(a.intersection(b)))
func(list(a.difference(b)))
func(list(b.difference(a)))