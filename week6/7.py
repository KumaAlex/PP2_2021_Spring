l = []
with open("input.txt", "r") as f:
    for line in f: l.append(line)
for i in l: print(i, end="")