
def selection_sort(arr):
    try:
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    except:
        return False

# print(selection_sort([5, 3, 6, 2, 10]))  # [2, 3, 5, 6, 10]
# print(selection_sort([5, 3, 6, 2, 10, 1])) # [1, 2, 3, 5, 6, 10]
# print(selection_sort(['b', 'g', 'a'])) # ['a', 'b', 'g']
# print(selection_sort(['b', 'g', 'a', 'c', 'd'])) # get False because of mixed types