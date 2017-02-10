"""
Jhonatan da Silva
Last Updated version :
Thu Feb  9 22:50:22 2017
Number of code lines: 
8
"""
import func 

def test_read():
    assert len(func.read('./test.txt'))

def test_write():
    func.write('./testWrite.txt',['1','2','3'])
    assert len(func.read('./testWrite.txt')) > 0
