count = 0
with open("input.txt", "r") as f: 
    for line in f: count += 1
x = count - int(input())
with open("input.txt", "r") as f: 
    for line in f:
        x -= 1
        if x < 0: print(line, end="")