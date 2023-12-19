def SelectionSort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


print(SelectionSort([47, 56, 34, 23, 86, 43, 65]))


# Here what happends is that using the variable understands at which index position largest value(as per condition)
# lies . Then value of the variable amd position of elements will be changed

#Complexity - O(n^2)
