#binary cross entropy

import numpy as np

def entropy(y,p):
    return -np.mean(y*np.log(p)+(1-y)*np.log(1-p))

a = np.random.randint(0, 2, 25)   
b = np.random.random(25)            
print(a)
print(b)
print(entropy(a, b))