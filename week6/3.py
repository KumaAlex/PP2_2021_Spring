txt = open("input.txt", "a")
txt.write(input())
txt.close()
txt = open("input.txt", "r")
print(txt.read())
txt.close()