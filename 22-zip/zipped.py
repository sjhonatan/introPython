""" assumes x and y are arrays of same length
    the zip function takes two arrays and put the i-th
    element of x with the i-th element of y in a tuple """
import numpy as np

x = np.array([1,2,3,4])
y = np.array([1,2,3,4])

zipped = list(zip(x,y))
print(zipped)

