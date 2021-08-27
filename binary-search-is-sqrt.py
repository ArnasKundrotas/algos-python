# Binary search
# Is X -> square 16 -> Yes, 20 -> No // Cannot use sqrt()


def is_a_square(x):
    left = 0
    right = x

    while left <= right:
        mid = left + (right - left)//2
        if x == mid * mid:
            print ("Yes: \n")
            print (x)
            return mid
        if x > mid * mid:
            left = mid + 1
        else:
            right = mid - 1
    print("No")
    return None

print (is_a_square(16))
print (is_a_square(1))
print (is_a_square(23))
print (is_a_square(132))
print (is_a_square(3045025))
print (is_a_square(91827180900))