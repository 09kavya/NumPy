#find all the number are greater than 50 and even


import numpy as np
a=np.random.randint(1,100,24).reshape(6,4)

b=a[(a>50) &(a%2==0)]
print(b)