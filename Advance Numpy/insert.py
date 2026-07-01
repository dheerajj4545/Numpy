# np.insert(array,index,value,axis=None)
# array-original array
# index-
# value-
# axis-
# axis=0,row-wise
# axis=1,col-wise

import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)
new_arr=np.insert(arr,3,100)
print(new_arr)