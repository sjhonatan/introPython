"""
Jhonatan da Silva
Last Updated version :
Thu Feb  9 22:56:52 2017
Number of code lines: 
6
"""
x = ['1','iosjaio', 'isajs', 'su90190u2' , '', '1', '', '', '', '', '', '', '21-09']

clean = lambda x: x if len(x) > 0 else 'empty' 

y = list(map(clean,x))
print(y)
