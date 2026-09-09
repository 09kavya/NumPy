#sigmoid
import numpy as np
def sigmoid(a):
    return 1/(1+ np.exp(-a))
a=np.arange(10)
print(sigmoid(a))