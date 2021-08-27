##############
# UNSOLVED 
##############

# Binary search
# Rotated arr
# Sorted arr [2,3,6,7,9,15,19] was rotated (shifted) 
# arr:      [6,   7,  9,  15, 19, 2,  3]
# index:     0    1   2   3   4   5   6 
#           left         mid         right
#                            mid     right
#                            ans
# find smallest element index in rotated arr

def find_sm_e(arr):
    left = 0
    right = len(arr) - 1 # 6
    ans = None

    while left <= right:
        mid = left + (right-left)//2 # 3 / 5
        if arr[mid] > arr[left]: # 15 > 6 / 2 > 19
            left = mid + 1 # 4
            ans = left # 3
        else:
            right = mid - 1
            ans = right
    return ans

print (find_sm_e([6,7,9,15,19,2,3])) # 5
print (find_sm_e([6,7,9,15,1,2,3])) # 4
print (find_sm_e([6,7,9,0,1,2,3])) # 3
print (find_sm_e([6,7,1,2,3,4,5])) # 2