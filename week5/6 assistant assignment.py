l = [int(i) for i in input().split()]
a, b = [int(i) for i in input().split()]
print([i in range(a,b) for i in l])