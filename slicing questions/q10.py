"""Checkerboard Pattern
Given:
a = np.arange(1, 17).reshape(4,4)
extract:
[[ 1,  3],
 [ 9, 11]]
and then separately extract:
[[ 2,  4],
 [10, 12]]
using slicing."""
import numpy as np
a=np.arange(1, 17).reshape(4,4)
print(a)
b=a[0:4:2,0:4:2]
print(b)
c=a[0:3:2,1:4:2]
print(c)
