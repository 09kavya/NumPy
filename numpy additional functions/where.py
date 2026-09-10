#give the index who is greter than 50
import numpy as np


a = np.random.randint(1, 101, 12)
print(a)
b=np.where(a>50)
print(b)