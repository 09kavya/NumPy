import numpy as np 

a=np.arange(12).reshape(3,4)
b=np.arange(12,24).reshape(3,4)

c=np.hstack((a,b))
print(c)