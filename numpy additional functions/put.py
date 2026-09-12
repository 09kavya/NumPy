import numpy as np

a = np.random.randint(1, 101, 12)
print(a)
b=np.put(a,[0,1],[110,130])
print(a)