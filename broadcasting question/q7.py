#Normalize Each Column
import numpy as np

a = np.array([[3, 4],
              [5, 12]])

norm = np.linalg.norm(a, axis=0, keepdims=True)

b = a / norm

print(b)