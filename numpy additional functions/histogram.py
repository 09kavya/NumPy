import numpy as np


a = np.random.randint(1, 101, 12)
print(a)
b=np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90])
print(b)