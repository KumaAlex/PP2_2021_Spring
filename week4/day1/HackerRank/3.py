import re
x = re.findall(r"[AEIOUaeiou][AEIOUaeiou]+", str(input()))
if x:
    for i in x: print(i)
else: print("-1")