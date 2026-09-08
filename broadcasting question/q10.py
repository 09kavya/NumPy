"""Nearest Point to Origin 
Given an n × d matrix of points, calculate the Euclidean distance of every point from the origin and return the index of the closest point."""
import numpy as np
points = np.array([[1,2], [3,4], [5,6]])
point=np.array([0,0]) 
dif=points-point
distance=np.sqrt(np.sum(dif**2,axis=1))
index = np.argmin(distance)
print(distance)
print(index)