# Binary search
# Is X -> square 16 -> Yes, 20 -> No // Cannot use sqrt()


def is_a_square(x):
    left = 0
    right = x
    #[0, 16]

    while left <= right:
        mid = left + (right - left)//2 #8
        if x == mid * mid: # 16 == 8 * 8
            return mid
        if x > mid * mid: # 16 > 8 * 8
            left = mid + 1
        else: # 16 < 8 * 8
            right = mid - 1 # 15
    return None

print (is_a_square(16))
print (is_a_square(1))
print (is_a_square(23))
print (is_a_square(132))
print (is_a_square(3045025))
print (is_a_square(91827180900))