# Binary search
# Find first value >=X

def find_first_val_x(arr, x) :
    left = 0
    right = len(arr) - 1 # 6
    ans = None

    while left <= right:
        mid = left + (right-left)//2 # 3 / 2 / 0
        if arr[mid] == x: # 
            return mid
        if arr[mid] > x: # 6 > 4 / 5 > 4 /
            ans = mid # 3 / 2
            right = mid - 1 # 5 / 1
        else:  # 2 < 4
            left = mid + 1 # 
    return ans

print (find_first_val_x([2,3,5,6,8,10,12], 4))