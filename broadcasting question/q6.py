#Given a matrix, subtract the mean of each row from every element of that row using broadcasting.

import numpy as np
a=np.arange(9).reshape(3,3)
b=np.mean(a)
print(a)
print(b)
print(a-b)