s = input()
a, b = [0, 0]
for i in range(len(s)):
    if s[i] >= 'A' and s[i] <= 'Z': a += 1
    else: b += 1
print("No. of Upper case characters : " + str(a))
print("No. of Lower case Characters : " + str(b))