def InsertionSort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while temp < nums[j] and j > -1:
            nums[j + 1] = nums[j]
            nums[j] = temp
            j -= 1
    return nums


print(InsertionSort([45, 34, 23, 56, 78, 33, 5]))

# Here comparison starts from 1st index position with previous and then move forward with comparing 
#continues with previous elements .

#Complexity - O(n^2)
