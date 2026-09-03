import numpy as np 

a=np.arange(12).reshape(3,4)


c=np.hsplit(a,2)
print(c)