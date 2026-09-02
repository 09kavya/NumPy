#mean , median , standard deviation , varience

import numpy as np

a1=np.random.random((3,3))
a1=np.round(a1*100)
print(a1)

a=np.mean(a1)
print(a)
a=np.median(a1)
print(a)
a=np.std(a1)
print(a)
a=np.var(a1)
print(a)