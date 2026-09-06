#Given an n × m matrix and an n-element array, add the array to every column using broadcasting.

import numpy as np

a=np.arange(9).reshape(3,3)
b=np.arange(3).reshape(3,1)
print(a+b)