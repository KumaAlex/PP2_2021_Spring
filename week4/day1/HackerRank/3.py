import re
txt = str(input())
OK = True
items = list()
x = re.compile(r"(?P<ans>[AEIOUaeiou][AEIOUaeiou]+)[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]")
for i in re.finditer(x, txt): items.append(i.group("ans"))
for i in items:
    print(i)
    OK = False
if OK:
    print("-1")