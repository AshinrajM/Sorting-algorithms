def BubbleSort(nums):
    n = len(nums)

    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


print(BubbleSort([5, 2, 5, 4, 12, 65, 34]))


# In bubble sort this sorting is done by comparing two adjacent elements and if they satisfy the condition
# they swaps their indices.So In the given after first iteration nums the largest value(Bases on the condition) 
# will be at the right end of the array.This process continues and array will get sorted

#Complexity - O(n^2)