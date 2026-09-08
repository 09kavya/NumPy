#Row-wise maximum difference

import numpy as np

a=np.random.random((9)).reshape(3,3)
b=np.round(a*100)
print(b)
b=np.min(b)
print(b)