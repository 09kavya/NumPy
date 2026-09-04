#find all the even number

import numpy as np
a=np.random.randint(1,100,24).reshape(6,4)

b=a[a%2==0]
print(b)