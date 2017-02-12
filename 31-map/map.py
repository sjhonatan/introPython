#!usr/bin/env
"""
Jhonatan da Silva
Last Updated version :
Sun Feb 12 21:21:45 2017
Number of code lines: 
6
"""
x = ['1','iosjaio', 'isajs', 'su90190u2' , '', '1', '', '', '', '', '', '', '21-09']

clean = lambda x: x if len(x) > 0 else 'empty' 

y = list(map(clean,x))
print(y)
