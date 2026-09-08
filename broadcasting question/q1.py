#Add Row Vector to Matrix Given an n × m matrix and an m-element array, add the array to every row using broadcasting.

import numpy as np
a=np.arange(3)
b=np.arange(9).reshape(3,3)
print(a)
print(b)
print(a+b)