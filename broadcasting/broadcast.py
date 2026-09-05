#sum of two no. whith different size

import numpy as np

a=np.arange(6).reshape(2,3)
print(a)
b=np.arange(3).reshape(1,3)
print(b)
print(a+b)
c=np.arange(6).reshape(2,3)+np.arange(3)
print(c)