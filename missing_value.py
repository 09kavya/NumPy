#working with missing value  #removes missing values

import numpy as np
a=np.array([1,2,3,4,np.nan,5,6])

#boolean indexing
b=a[~np.isnan(a)]
print(b)

