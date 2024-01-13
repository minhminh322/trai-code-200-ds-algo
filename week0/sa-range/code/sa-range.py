from static_array import *

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    # In practical, you can use length = abs(end - start) + 1, but remember
    # Python built-in libraries are not allowed in this problem.
    
    if start < end:
        length = end - start + 1
    else:
        length = start - end + 1
    range_arr = StaticArray(length)
    for index in range(0, length):
        if start < end:
            range_arr[index] = start + index
        else:
            range_arr[index] = start - index
    return range_arr

# ------------------- TESTING -----------------------------------------

if __name__ == "__main__":

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")
