#Normalize Each Row Given a matrix, subtract the mean of each row from every element of that row using broadcasting.
 
import numpy as np

a = np.array([[3, 4],
              [5, 12]])

norm = np.linalg.norm(a, axis=1, keepdims=True)

b = a / norm
c=np.mean(a)
print(b-c)


