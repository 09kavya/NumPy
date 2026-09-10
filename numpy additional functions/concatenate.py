import numpy as np

a=np.arange(9).reshape(3,3)
b=np.arange(10,19).reshape(3,3)

c=np.concatenate((a,b),axis=0)
print(c)