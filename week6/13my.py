with open("text", "r") as f:
    with open("copy", "w") as d:
        for i in f: d.write(i)