import numpy as np

a1=np.random.random((3,3))
a1=np.round(a1*100)
print(a1)

a=np.max(a1)
print(a)
a=np.min(a1)
print(a)
a=np.sum(a1)
print(a)
a=np.prod(a1)
print(a)