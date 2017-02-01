"""
Jhonatan da Silva
Last Updated version :
Tue Jan 31 22:35:35 2017
Number of code lines: 
19
"""
import matplotlib.pyplot as plt
import numpy as np

x_axis = np.arange(9)
y_axis = np.arange(9)

plt.figure(figsize=(20,20))
plt.scatter(x_axis, y_axis)
plt.grid(True)
plt.show()

print('pronto')

novo_y_axis = 5*y_axis
plt.figure(figsize=(20,20))
plt.scatter(x_axis, novo_y_axis)
plt.axes().set_aspect('equal','datalim')
plt.grid(True)
plt.show()
