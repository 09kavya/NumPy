import numpy as np

a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)

a3=a1+4
print(a3)
a3=a2*2
print(a3)
a3=a1/4
print(a3)
a3=a2**2
print(a3)
a3=a1/6
print(a3)
a3=a2//4
print(a3)