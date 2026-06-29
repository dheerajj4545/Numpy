# .ravel()->used to convert mutidimensional array into 1d by modifying the original array
# .flatten()->used to convert mutidimensional array into 1d by giving a copy of the original array

import numpy as np

arr_2d=np.array([[1,2,3],[4,5,6]])

print(arr_2d.ravel())
print(arr_2d.flatten())