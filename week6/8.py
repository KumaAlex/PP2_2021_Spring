with open("input.txt", "r") as f:
    words = f.read().split()
    l = words[0]
    for i in words:
        if len(l) < len(i): l = i
    print(l)