def f1(a):
    def f2(b):
        nonlocal a
        a += 1
        return(a+b)
    return f2
ans = f1(int(input()))
print(ans(int(input())))