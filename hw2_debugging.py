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

def recombine(left_arr, right_arr):
    """
    Merge Sort helper
    """
    left_index = 0
    right_index = 0
    mergeArr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            mergeArr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            mergeArr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        mergeArr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        mergeArr[left_index + right_index] = left_arr[i]

    return mergeArr

arr_in = rand.random_array([None] * 20)
arr_out = merge_sort(arr_in)

print(arr_out)
