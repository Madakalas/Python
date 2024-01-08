def f1():
    print("GM")
    def f2():
        print(f2)
    return f2
x=f1()
print(x)