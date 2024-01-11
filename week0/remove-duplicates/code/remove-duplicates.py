from static_array import *

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    if arr.length() <= 1:
        return arr  # No duplicates to remove
    
    new_arr = StaticArray(arr.length())
    new_arr_index = 0
    new_arr[0] = arr[0]
    for i in range(1, arr.length()):
        if new_arr[new_arr_index] != arr[i]:
            new_arr_index += 1
            new_arr[new_arr_index] = arr[i]
    
    return new_arr

# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":
    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)