#Add Column Vector to Matrix

import numpy as np

a=np.arange(9).reshape(3,3)
b=np.arange(3).reshape(3,1)
print(a+b)