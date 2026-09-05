#broadcasting not run and give an error

import numpy as np

a=np.arange(12).reshape(3,4)
b=np.arange(3)

print(a+b)