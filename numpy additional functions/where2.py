#all the even no. replace with 0


import numpy as np


a = np.random.randint(1, 101, 12)
print(a)
b=np.where(a%2==0,0,a)
print(b)