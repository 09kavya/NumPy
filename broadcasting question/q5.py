#Row-wise maximum difference For every row, subtract its minimum value from all elements using broadcasting.

import numpy as np

a=np.random.random((9)).reshape(3,3)
b=np.round(a*100)
print(b)
c=np.min(b,axis=1,keepdims=True)
print(c)

print(b-c)