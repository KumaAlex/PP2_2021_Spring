import re
n = int(input())
for i in range(n):
    x = input()
    print(bool(re.search(r"^[+-]?\d*[.]\d+$", x)))