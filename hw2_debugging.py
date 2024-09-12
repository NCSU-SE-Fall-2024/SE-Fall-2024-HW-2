"""
This function sorts arrays of numbers using merge sort technique
"""
import rand

def merge_sort(arr):
    """
    Merge Sort 
    """
    if len(arr) == 1:
        return arr

    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, rightArr):
    """
    Merge Sort helper
    """
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(left_arr) + len(rightArr))
    while leftIndex < len(left_arr) and rightIndex < len(rightArr):
        if left_arr[leftIndex] < rightArr[rightIndex]:
            rightIndex += 1
            mergeArr[leftIndex + rightIndex] = left_arr[leftIndex]
        else:
            leftIndex += 1
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]

    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + rightIndex] = rightArr[i]

    for i in range(leftIndex, len(left_arr)):
        mergeArr[leftIndex + rightIndex] = left_arr[i]

    return mergeArr

arr_in = rand.random_array([None] * 20)
arr_out = merge_sort(arr_in)

print(arr_out)
