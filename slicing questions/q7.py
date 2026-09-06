#Given a matrix, reverse the order of rows using slicing.

import numpy as np

a=np.arange(9).reshape(3,3)
print(a)
b=a[::-1,::-1]
print(b)