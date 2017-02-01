"""
Jhonatan da Silva
Last Updated version :
Tue Jan 31 22:35:53 2017
Number of code lines: 
8
"""
def usingYield():
    for i in range(4):
        yield i*i

x = createGenerator()

for i in x:
    print(i)
