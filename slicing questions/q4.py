# Given an nXm matrix , extract its 1st and last row , first column and last column using slicing

import numpy as np
a=np.arange(12).reshape(3,4)
print(a)
print(a[0::2,0::2])