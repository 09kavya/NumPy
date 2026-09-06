#Given an n × m matrix and an m-element array, add the array to every row using broadcasting.

import numpy as np
a=np.arange(9).reshape(3,3)
b=np.arange(3).reshape(1,3)
print(a+b)