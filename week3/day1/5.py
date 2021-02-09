from collections import deque
x = [int(i) for i in input().split()]
k = int(input())
x = deque(x)
x.rotate(k)
for i in x:
    print(i, end = " ")