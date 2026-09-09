#sort 1d and 2d array


#1d
import numpy as np
a=np.random.randint(1,100,20)
print(a)
b=np.sort(a)     #ascending order
print(b)

b=np.sort(a)[::-1]    
print(b)         # descending order

#2d

a=np.random.randint(1,100,20).reshape(4,5)
b=np.sort(a)
print(a)
b=np.sort(a,axis=1)     #ascending order
print(b)

b=np.sort(a,axis=0)[::-1]
print(b) 