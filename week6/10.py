d = {}
with open("input2.txt", "r") as f:
    words = f.read().split()
for i in words:
    if i in d.keys(): d[i] += 1
    else: d[i] = 1
l = list(d.items())
l.sort(key = lambda x: x[1], reverse=True)
for i in l: 
    print(i[0] + " : " + str(i[1]))