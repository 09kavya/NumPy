#sum with broadcasting rules


import numpy as np

a=np.arange(12).reshape(4,3)
b=np.arange(3)

print(a+b)