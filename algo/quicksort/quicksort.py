def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] # floor division
    left = [x for x in arr if x < pivot] # list comprehension
    middle = [x for x in arr if x == pivot] # list comprehension
    right = [x for x in arr if x > pivot] # list comprehension
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))  # [1, 1, 2, 3, 6, 8, 10]
