import numpy as np

a1=np.random.random((3,3))
a1=np.round(a1*100)
a2=np.arange(12).reshape(3,4)

a3=np.dot(a1,a2)
print(a3)