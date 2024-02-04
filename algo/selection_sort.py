def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# print(selection_sort([5, 3, 6, 2, 10]))
# print(selection_sort([5, 3, 6, 2, 10, 1]))