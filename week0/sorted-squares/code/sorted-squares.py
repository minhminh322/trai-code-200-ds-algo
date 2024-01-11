from static_array import *

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    squares_arr = StaticArray(arr.length())
    left, right = 0, arr.length() - 1
    squares_arr_index = squares_arr.length() - 1
    while left <= right:
        if arr[left] ** 2 < arr[right] ** 2:
            squares_arr[squares_arr_index] = arr[right] ** 2
            right -= 1
        else:
            squares_arr[squares_arr_index] = arr[left] ** 2
            left += 1
        squares_arr_index -= 1
        
    return squares_arr

# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":
    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')