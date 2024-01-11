from static_array import *

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    if arr.length() == 0:
        return arr  # Handle empty array case

    min_val = max_val = arr[0]
    for index in range(arr.length()):
        if min_val > arr[index]:
            min_val = arr[index]
        if max_val < arr[index]:
            max_val = arr[index]

    arr_range = max_val - min_val + 1
    count_arr = StaticArray(arr_range)  
    for i in range(count_arr.length()):
        count_arr[i] = 0 # Initialize count_arr with zeros

    for index in range(arr.length()):
        count_arr[arr[index] - min_val] += 1

    result_arr = StaticArray(arr.length())
    result_index = 0
    for i in range(count_arr.length() - 1, -1, -1):
        count = count_arr[i]
        while count > 0:
            result_arr[result_index] = i + min_val
            result_index += 1
            count -= 1

    return result_arr

# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":
    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')