import numpy as np

a = np.random.randint(1, 101, 12)
print(a)
b=np.clip(a,a_min=25,a_max=70)
print(b)