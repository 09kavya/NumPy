"""Given:
a = np.arange(1, 17).reshape(4,4)
extract:
[[1, 3],
 [9, 11]]
using slicing only."""

import numpy as np
a=np.arange(1, 17).reshape(4,4)
print(a)
b=a[0:4:2,0:4:2]
print(b)