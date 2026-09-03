import numpy as np

a=np.arange(12)
b=np.arange(12).reshape(3,4)
c=np.arange(27).reshape(3,3,3)

print(a)
print(b)
print(c)

#1d array slicing
print("1D element")
print(a[2:5])
print(a[2:5:2] )#jump with 2 , give alternate number

#2d array slicing
print("2D element")
print(b[0,:]) # 0 index row ke sare element(:)
print(b[:,2] ) #2nd column ke sare element
print(b[1:,1:3])#5 6,9 10 aayega mtlb 1 ke baad vale sare row or 1 or 2 column
print(b[::2,::3])#4 corner element aa jayenge row me 2 ka junp aa rha h and column me 3 ka
print(b[::2,1::2])#1 9,3 11 element
print(b[1,::3])# 4 7
print(b[0:2,1:])


#3d array slicing
print("3D element")
print(c[1])#2nd 3d array
print(c[::2])#1st and last 3d array
print(c[0,1:])#1st 3d array 2nd row all the columns
print(c[1,:,1])#2nd 3d array center column
print(c[2,1:,1:])
print(c[0::2,0,0::2])