x = input()
with open("text", "a", encoding="utf8") as f:
    for i in x: f.write(i)
with open("text", "r", encoding="utf8") as f:
    for i in f: print(i)