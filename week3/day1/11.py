import sys
l = (str(sys.stdin.read()).split())
d = {}
for i in l:
	if i in d.keys(): d[i] += 1
	else: d[i] = 1
q = list(d.items())
q.sort()
q.sort(reverse = True, key = lambda i: i[1])
for i in q:
	print(i[0])