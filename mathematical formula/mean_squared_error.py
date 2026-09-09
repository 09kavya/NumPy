#mean squared error

import numpy as np

def mean(actual,predicted):
    return np.mean((actual-predicted)**2)

actual=np.random.randint(1,50,25)
predicted=np.random.randint(1,50,25)
print(actual)
print(predicted)

print(mean(actual,predicted))