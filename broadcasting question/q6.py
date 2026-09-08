"""distance from a Point
Given points:
points = np.array([[1,2], [3,4], [5,6]])
and point [2,3], calculate Euclidean distance of every point from [2,3] using broadcasting."""


import numpy as np
points = np.array([[1,2], [3,4], [5,6]])
point=np.array([2,3]) 
dif=points-point
distance=np.sqrt(np.sum(dif**2,axis=1))
print(distance)