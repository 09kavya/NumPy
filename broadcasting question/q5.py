#Normalize Each Row
 
import numpy as np

a = np.array([[3, 4],
              [5, 12]])

norm = np.linalg.norm(a, axis=1, keepdims=True)

b = a / norm

print(b)