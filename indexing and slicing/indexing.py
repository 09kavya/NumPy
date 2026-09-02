import numpy as np

a=np.arange(12)
b=np.arange(12).reshape(3,4)
c=np.arange(8).reshape(2,2,2)

print(a)
print(b)
print(c)

#indexing of 1d array
a=a[-1]  #give last element
print(a)

#indexing of 2d array
b=b[1,2]  #6
print(b)

#indexing of 2d array
c=c[1,0,0]  #4
print(c)