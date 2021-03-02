n = int(input())
cnt = 0
for i in range(1, n):
    if (n % i == 0): cnt += 1
if cnt == 1: print("True")
else: print("False")