import re
txt = str(input())
OK = True
items = []
x = re.compile(r".+(?P<ans>[AEIOUaeiou][AEIOUaeiou]+).+")
for i in re.finditer(x, txt): items.append(i.group("ans"))
for i in items:
    print(i)
    OK = False
if OK:
    print("-1")
print(txt)