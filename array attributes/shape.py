import numpy as np

a1=np.arange(10,dtype=np.int32)
a2=np.arange(12,dtype=np.int32).reshape(3,4)
a3=np.arange(8,dtype=np.int32).reshape(2,2,2)

a=a3.shape
print(a)