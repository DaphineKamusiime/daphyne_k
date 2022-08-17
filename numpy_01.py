import numpy as np
my_array=np.arange(8)#printing all integers less than 8
my_array=np.arange(1,8)#printing all integers between 1 and 8
my_array=np.arange(1,8,0.5)
my_array=np.arange(-1,9.25,0.5)
print(my_array)
print(type(my_array))
##converting  alist into an array
from_list=np.array([1,2,3])
print(from_list)
##Arrays use less space than lists
print(type(from_list[0]))
print(type(from_list[0]),dtype=np.int8)##specifying number of bits
##dealing with a 2D array
from_list=np.array([[1,2,3,4][6,9,8,0]])
from_list=np.array((np.arrange(1,2,3,4)))
print(from_list)
np.array((np.arrange[0,2,4,6,8],[1,3,5,7,9]))
print(from_list)