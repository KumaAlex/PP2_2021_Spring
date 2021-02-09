x = input().split()
k = int(input())
if k > 0:
    for i in range(len(x)-k, len(x)):
        print(x[i], end = " ")
    for i in range(len(x)-k):
        print(x[i], end = " ")
else:
    for i in range(-1*k, len(x)):
        print(x[i], end = " ")
    for i in range(-1*k):
        print(x[i], end = " ")