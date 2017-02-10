"""
Jhonatan da Silva
Last Updated version :
Thu Feb  9 22:50:12 2017
Number of code lines: 
11
"""
def read(path):
    with open(path,'r') as f:
        return f.read().splitlines()

def write(path,data):
    with open(path,'w') as f:
        if type(data) == list:
            [f.write(line + '\n') for line in data]
        else:
            f.write(data + '\n')

