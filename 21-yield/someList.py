def usingYield():
    for i in range(4):
        yield i*i

x = createGenerator()

for i in x:
    print(i)
