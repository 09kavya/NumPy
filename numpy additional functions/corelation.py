import numpy as np

a=np.array([10000,50000,80000,60000,20000])
b=np.array([1,2,3,4,2])

c=np.corrcoef(a,b)
print(c)