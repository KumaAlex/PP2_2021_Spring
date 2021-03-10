with open("input.txt") as f, open("input2.txt") as f1:
    for l, l1 in zip(f, f1):
        print(l + l1, end="")