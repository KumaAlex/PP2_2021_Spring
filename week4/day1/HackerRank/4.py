import re
for i in range(int(input())):
    x = str(input())
    ans = re.search(r"^[789]\d{9}$", x)
    if ans: print("YES")
    else: print("NO")