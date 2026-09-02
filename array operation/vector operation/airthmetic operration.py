import numpy as np

a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)

a3=a1+a2
print(a3)
a3=a2*a1
print(a3)
a3=a1/a2
print(a3)
a3=a2**a1
print(a3)
a3=a1/a2
print(a3)
a3=a2//a1
print(a3)