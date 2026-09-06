#given : a=np.arange(1,26).reshape(5,5) extract the ceter 3x3 matrix

import numpy as np

a=np.arange(1,26).reshape(5,5)
print(a)
b=a[1:4,1:4]
print(b)