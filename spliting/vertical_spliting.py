import numpy as np

a=np.random.random((12)).reshape(3,4)
b=np.round(a*100)

e=np.vsplit(b,3)
print(e)