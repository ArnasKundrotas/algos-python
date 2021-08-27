# Binary search
# Find arr number index

def first_arr_value(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

print (first_arr_value([2,3,5,6,8,10,12], 8))
print (first_arr_value([2,3,5,6,8,10,12,500,658,999], 9))