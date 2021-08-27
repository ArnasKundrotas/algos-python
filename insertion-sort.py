def insertion_sort(arr): # arr -> [5,4,3,2,1]

	for i in range(1, len(arr)): 
    # loop 4 times from 1 till 4 -> 1,2,3,4
    # len(arr) -> 4 -> 0,1,2,3,->4

		key = arr[i] # 4 

		j = i-1 # 0

		while j >=0 and key < arr[j] : # while 0 >= 0 and 4 < 5
				arr[j+1] = arr[j] # 4 = 5
				j -= 1 # -1
                
		arr[j+1] = key # 4 = key


arr = [5,4,3,2,1]
new_arr = []

for i in range(len(arr)):
	new_arr.append(arr.pop(insertion_sort(arr)))

print ()
