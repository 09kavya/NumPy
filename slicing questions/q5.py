#Given a matrix, extract its top left quadrant using slicing


import numpy as np

a=np.arange(16).reshape(4,4)
print(a)
b=a[0:2,0:2]
print(b)