import os
print("What is it?\n1 - directory\n2 - file")
n = int(input())
if n == 2: 
    print("What do you need?\n1 - delete\n2 - rename\n3 - add content\n4 - rewrite")
    a = int(input())
    print("Print file name: ")
    s = input()
    if a == 1: os.remove(s)
    if a == 2: os.rename(s, input())
    if a == 3:
        with open(s, 'a') as f:
            f.write(input())
    if a == 4: 
        with open(s, 'w') as f: 
            f.write(input())
if n == 1: 
    print("What do you need?\n1 - rename directory\n2 - print number of files\n3 - print number of directories\n4 - add file to this directory\n5 - add new directory to this directory")
    a = int(input())
    if a == 1: 
        s = input()
        os.rename(s, input())
    if a == 2 or a == 3: 
        path, dirs, files = next(os.walk(r'C:\Users\Мои документы\Desktop\Универ\1 курс 2 семестр\PP2\alex\week6\part2'))
        if a == 2: print(len(files))
        if a == 3: print(len(dirs))
    if a == 4:
        with open(input(), 'w') as f: pass
    if a == 5: os.mkdir(input())