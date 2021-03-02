import re
for i in range(int(input())):
    s = str(input())
    x = re.search(r"[A-Za-z]+\s[<]{1}[a-zA-Z][a-zA-Z0-9._-]+@{1}[a-zA-Z]+[.][a-zA-Z]+[>]{1}$", s)
    if x: print(s)