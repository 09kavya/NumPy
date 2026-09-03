#numpy vs list according to memory

#list
import sys
a=[i for i in range(10000000)]
b=sys.getsizeof(a)
print(b)

#numpy
import numpy as np
a=np.arange(10000000,dtype=np.int32)
b=sys.getsizeof(a)
print(b)