txt = open("input.txt" , 'r' , encoding="utf-8")
for i in range(int(input())): print(txt.readline(), end = "")
txt.close()