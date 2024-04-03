
def binary_search(arr, target):
    left, right = 0, len(arr) - 1 # set the left and right pointers
    while left <= right: # while left pointer is less than or equal to right pointer
        mid = left + (right - left) // 2 # calculate the mid point of the array to check if the target is in the left or right side
        if arr[mid] == target: # if the mid point is the target, return the mid point
            return mid
        elif arr[mid] < target: # if the mid point is less than the target, move the left pointer to the right
            left = mid + 1
        else:
            right = mid - 1
    return -1 # if the target is not found, return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)) # 4

# time complexity: O(log n)