import numpy as np

a=np.random.random((12)).reshape(3,4)
b=np.round(a*100)
c=np.random.random((12)).reshape(3,4)
d=np.round(c*100)
e=np.vstack((b,d))
print(e)