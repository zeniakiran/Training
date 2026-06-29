import numpy as np

# Create Array

# ndarray
array1 = np.array([1,2,3,4,5,6,4,4]) #1D 

array2 = np.array([10,11,12,13,14]) 

#print(array1)
# Access Array Elements

#print(array1[2])

# Slicing Array
# [i, n-1]
slicedArray = array1[0:3] # first index will be includes, last ind would be excluded
#print(slicedArray)

# Checking data types of array
#print(array2)

# Create array with data type
array3 = np.array(["a", "b", "c"], dtype="S1") 

# Shape array

array_2d = np.array([[1,2,3], [4,5,6]])
#[ [1   2    3]
# [4,  5,   6] ]
#
#print(np.shape(array_2d))

# Reshape Array (2,3) = 6
#print(array1.reshape(3,2)) # 3 rows, 2 cols

# Iterating Array
for elem in array1:
    print(elem)
#
# Joining Arrays (tuple)
combined_array = np.concatenate((array1, array2))
#print("Combined Array: ", combined_array)

# Searching Array

searched_elem = np.where( array1 == 4 )
#print(searched_elem)

# Generate Random Number
# Sort Arrays

sorted_array = np.sort(array1)
print("Sorted Array:", sorted_array)

# Add/Subtract/Multiple/Divide two arrays

arr1= np.array([1,1,1]) 
arr2 = np.array([10,10,10])

add = np.add(arr1, arr2)
print(add) # [11, 11, 11]

subtract = np.subtract(arr2, arr1) # [-9,-9,-9]
print(subtract)

multipluy = np.multiply(arr1, arr2)
print(multipluy)

divide = np.divide(arr2, arr1)
print(divide)
#
# Create 2d arrays


