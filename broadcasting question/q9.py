"""Outer Product 
Given two 1-D arrays a and b, calculate their outer product using only broadcasting, without np.outer()."""
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5])
c=a[:,None]*b
print(c)