import numpy as np
a=np.arange(9)
b=np.arange(9).reshape(3,3)

c=np.append(a,12)
d=np.append(b,np.ones((b.shape[0],1)),axis=1)

print(c)
print(d)