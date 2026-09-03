import numpy as np
c=np.arange(27).reshape(3,3,3)

for i in np.nditer(c):
    print(i)