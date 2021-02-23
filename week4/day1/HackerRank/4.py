import re
x = re.findall(r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm].*(?P<ans>[AEIOUaeiou][AEIOUaeiou]+).*[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]", str(input()))
if x:
    for i in x: print(i)
else: print("-1")