"""Pairwise Difference 
Given:
a = np.array([1, 4, 7])
generate a 3 × 3 matrix where:
result[i][j] = a[i] - a[j]"""

import numpy as np
a = np.array([1, 4, 7])
result=a[:,None]-a
print(result)