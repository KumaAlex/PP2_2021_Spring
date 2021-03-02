n = int(input())
print(sum([int(i) for i in range(1, n) if n % i == 0]) == n)