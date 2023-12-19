# 1======>>>
# In Quick Sort we are selecting an element as pivot and arranging its left and right sides.
# So what happends is that the array changes indices of elements as per pivot , Also on each recursion 
# pivot element will be changed.Here after every element is sorted in the last recursive call length becomes 1
# and condition is satisfied and returns the sorted data
# Time complexity - O(n^2) Space Complexity - O(n)

# def quicksort(data):
#     if len(data) <= 1:
#         return data

#     pivot = data[0]
#     left = [x for x in data[1:] if x <= pivot]
#     right = [x for x in data[1:] if x > pivot]

#     return quicksort(left) + [pivot] + quicksort(right)


# # Example usage
# data = [6, 5, 3, 1, 8, 7, 2, 4]
# sorted_data = quicksort(data)
# print(f"Sorted data: {sorted_data}")

#----------------------------------------------------------------------------------------


# 2=======>>>
# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# def partition(array, low, high):

# 	pivot = array[high]

# 	i = low - 1

# 	for j in range(low, high):
# 		if array[j] <= pivot:

# 			i = i + 1

# 			(array[i], array[j]) = (array[j], array[i])

# 	(array[i + 1], array[high]) = (array[high], array[i + 1])

# 	return i + 1

# def quickSort(array, low, high):
# 	if low < high:

# 		# Find pivot element such that
# 		# element smaller than pivot are on the left
# 		# element greater than pivot are on the right
# 		pi = partition(array, low, high)

# 		# Recursive call on the left of pivot
# 		quickSort(array, low, pi - 1)

# 		# Recursive call on the right of pivot
# 		quickSort(array, pi + 1, high)


# data = [1, 7, 4, 1, 10, 9, -2]
# size = len(data)
# quickSort(data, 0, size - 1)
# print('Sorted Array in Ascending Order:')
# print(data)
