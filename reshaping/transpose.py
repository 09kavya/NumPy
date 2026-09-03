import numpy as np

a=np.arange(12).reshape(3,4)
b=np.transpose(a)
print(b)
b=b.T #short way
print(b)