#numpy vs list according to speed

#list
import time

a=[i for i in range(10000000)]
b=[i for i in range(10000000,20000000)]
c=[]
start=time.time()
for i in range(len(a)):
    c.append(a[i]+b[i])

print(time.time()-start)


#numpy arrays

import numpy as np

a=np.arange(10000000)
b=np.arange(10000000,20000000)

c=a+b
start=time.time()
print(time.time()-start)