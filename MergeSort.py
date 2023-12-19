def MergeSort(arr):
    print("initial::", arr)
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = MergeSort(arr[:mid])
    print("left::", left)
    right = MergeSort(arr[mid:])
    print("right::", right)
    print("b:","left::", left, ":::right:", right)
    return Merge(left, right)

def Merge(left, right):
    print("a:","left::", left, ":::right:", right)
    combined = []
    print("merge:::::::::::::")

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1
    combined.extend(left[i:])
    combined.extend(right[j:])
    print("combined_b::::", combined)
    return combined


my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = MergeSort(my_list)
print("Sorted list:", sorted_list)

# Merge sort is a divide and conquer algorithm (Divide and conquer is actually 1- First the problem divided into
# smaller problems  2- solving sub problems by calling recursively until solved  3- combine the problems to get the final solution )
# Time complexity - O(nlogn)  Space complexity - O(n)










# def Merge(left, right):
#     combined = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             combined.append(left[i])
#             i += 1
#         else:
#             combined.append(right[j])
#             i += 1
#     while i < len(left):
#         combined.append(left[i])
#         i += 1
#     while j < len(right):
#         combined.append(right[j])
#         j += 1
#     return combined


# def MergeSort(arr):
#     if len(arr) == 1:
#         return arr
#     mid = int(len(arr) / 2)
#     left = MergeSort(arr[:mid])
#     right = MergeSort(arr[mid:])

#     return Merge(left, right)
