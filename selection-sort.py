# Selection sort
# Sort given array from lowest to highest values
# Selection sort is an in-place comparison sorting algorithm. 
# It has an O(n²) time complexity, which makes it inefficient on large lists.

# example arr [5,3,6,2,10]

def find_smallest_arr_value(arr):
    smallest_arr_value = arr[0] # 5
    smallest_arr_index = 0 

    print(arr)
    # [5, 3, 6, 2, 10]
    # [5, 3, 6, 10]
    # [5, 6, 10]
    # [6, 10]
    # [10]

    for i in range(1, len(arr)): # example [5,3,6,2,10] -> loops i -> 4 times
        #1.
        #2.
        #3.
        #4.
        if arr[i] < smallest_arr_value:
            
            smallest_arr_value = arr[i]
            smallest_arr_index = i

            # [5,3,6,2,10]
            # 1. arr[1]<arr[0] -> 3 < 5 -> smallest_arr_value = 3 -> smallest_arr_index = 1 -> print
            # 2. arr[2]<3 -> 6 < 3
            # 3. arr[3]<3 -> 2 < 3 -> smallest_arr_value = 2 -> smallest_arr_index = 3 -> print
            # 4. arr[4]<2 -> 10 < 2
            
            # [5,3,6,10]
            # 1. arr[1]<arr[0] -> 3 < 5 -> smallest_arr_value = 3 -> smallest_arr_index = 1 -> print
            # 2. arr[2]<3 -> 6 < 3
            # 4. arr[3]<3 -> 10 < 3
            
            # [5,6,10]
            # 1. arr[1]<arr[0] -> 6 < 5
            # 2. arr[2]<5 -> 10 < 5
            
            # [6,10]
            # 1. arr[1]<arr[0] -> 10 < 6
            
            # [10]
            
            print (smallest_arr_value, smallest_arr_index)

            # 3 1 -> [5,3,6,2,10]
            # 2 3 -> [5,3,6,2,10]
            # 3 1 -> [5,3,6,10]
     
    return smallest_arr_index # 3
    # 3 -> 2
    # 1 -> 3
    # 0 -> 5
    # 0 -> 6
    # 0 -> 10


def selec_sort(arr):
    new_arr = []
    for i in range(len(arr)): # example [5,3,6,2,10] -> loops i -> 0,1,2,3,4 -> 5 loops
        #0
        #1
        #2
        #3
        #4
        smallest_arr_value = find_smallest_arr_value(arr) 
        # 3 -> 2
        # 1 -> 3
        # 0 -> 5
        # 0 -> 6
        # 0 -> 10
        print(arr)
        # [5, 3, 6, 2, 10]
        # [5, 3, 6, 10]
        # [5, 6, 10]
        # [6, 10]
        # [10]
        new_arr.append(arr.pop(smallest_arr_value)) # arr.pop(arr index) -> 3,1,0,0,0
        #[2]
        #[2, 3]
        #[2, 3, 5]
        #[2, 3, 5, 6]
        #[2, 3, 5, 6, 10]
    return new_arr

print (selec_sort ([5,3,6,2,10])) 
# [2, 3, 5, 6, 10]

print (selec_sort ([5,3,6,2,10,95,87,63,42,59,156,2849,3254,1256,1,1,23,65])) 
# [1, 1, 2, 3, 5, 6, 10, 23, 42, 59, 63, 65, 87, 95, 156, 1256, 2849, 3254]

print (selec_sort ([5,3,6,2,10,95,87,63,42,59,156,2849,3254,1256,1,1,23,65,-1])) 
# [-1, 1, 1, 2, 3, 5, 6, 10, 23, 42, 59, 63, 65, 87, 95, 156, 1256, 2849, 3254]