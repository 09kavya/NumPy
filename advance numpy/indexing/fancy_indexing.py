#fancy indexing by rows
import numpy as np
a=np.arange(12).reshape(4,3)

b=a[[0,2,3]]
print(b)

#fancy indexing by columns
 
a=np.arange(24).reshape(6,4)
print(a)
b=a[:,[0,2,3]]
print(b)

#if i want 1st row 3rd row and 5thand 6th row and 1st column 3rd and 4th column

b=a[np.ix_([0,2,4,5],[0,2,3])]
print(b)


#if you want [0,0] , [2,2] ,[4,3] index value
b=a[[0,2,4],[0,2,3]]
print(b)
